import asyncio
import json
import os
import re
from datetime import datetime

import pytz
import websockets
from dotenv import load_dotenv

import coordinates
import countrycodes

load_dotenv(".env")

RELAY_HOST = "127.0.0.1"   # local only; the browser map connects here
RELAY_PORT = 8765
BATCH_SECONDS = 1.0        # how often the latest positions are pushed to the map

CLIENTS = set()            # connected map pages
latest = {}                # mmsi -> GeoJSON feature (only newest position per ship)

ANSI = re.compile(r"\x1b\[[0-9;]*m")
reset_color = "\033[0;0m"  # Resets formatting back to default


async def relay_handler(ws):
    """A map page connected; keep it registered until it disconnects."""
    CLIENTS.add(ws)
    try:
        await ws.wait_closed()
    finally:
        CLIENTS.discard(ws)


async def broadcaster():
    """Every BATCH_SECONDS, send each ship's newest position to all map pages."""
    while True:
        await asyncio.sleep(BATCH_SECONDS)
        if latest and CLIENTS:
            batch = list(latest.values())
            latest.clear()
            websockets.broadcast(CLIENTS, json.dumps(batch))


async def connect_ais_stream():
    asyncio.create_task(broadcaster())

    async with websockets.serve(relay_handler, RELAY_HOST, RELAY_PORT):
        print(f"Relay listening on ws://{RELAY_HOST}:{RELAY_PORT}")

        async with websockets.connect("wss://stream.aisstream.io/v0/stream") as ais:
            subscribe_message = {
                "APIKey": os.getenv("AISSTREAM_API_KEY"),
                "BoundingBoxes": [coordinates.world_box],
                "FilterMessageTypes": ["PositionReport"],
            }
            await ais.send(json.dumps(subscribe_message))

            async for message_json in ais:
                message = json.loads(message_json)

                # Safely check if the incoming message is actually a PositionReport
                if message.get("MessageType") != "PositionReport":
                    continue

                ais_message = message.get("Message", {}).get("PositionReport")

                # Double check that PositionReport exists in payload
                if not ais_message:
                    continue

                meta = message.get("MetaData", {})
                vessel_name = (meta.get("ShipName") or "Unknown").strip()
                current_time = datetime.now(pytz.timezone("Europe/Sofia"))
                ship_id = str(ais_message.get("UserID", "N/A"))
                lat = round(ais_message.get("Latitude", 0.0), 5)
                lon = round(ais_message.get("Longitude", 0.0), 5)

                # AIS uses out-of-range values for "position not available"
                if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    continue

                # Heading: 511 means "not available", fall back to course over ground
                heading = ais_message.get("TrueHeading")
                if heading is None or heading == 511:
                    heading = ais_message.get("Cog")
                    if heading is not None and heading >= 360:
                        heading = None

                country_code = ship_id[:3]  # Extracts first 3 digits from ship_id
                color = countrycodes.colors_dict.get(country_code, "")  # color+country string
                country = ANSI.sub("", color)  # "\033[92mBG" -> "BG"

                latest[ship_id] = {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [lon, lat]},  # GeoJSON is [lon, lat]
                    "properties": {
                        "mmsi": ship_id,
                        "name": vessel_name,
                        "heading": heading,
                        "sog": ais_message.get("Sog"),
                        "country": country,
                    },
                }

                log_str = (
                    f"[{current_time}] Name: {vessel_name} ShipId: {color} {ship_id}{reset_color} "
                    f"Latitude: {lat} Longitude: {lon}"
                )
                print(log_str)

                # File is automatically closed when leaving the 'with' block
                with open("logs.txt", "a", encoding="utf-8") as f:
                    f.write(log_str + "\n")


if __name__ == "__main__":
    asyncio.run(connect_ais_stream())
