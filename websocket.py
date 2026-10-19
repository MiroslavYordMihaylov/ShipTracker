import asyncio
import json
import os
from datetime import datetime
import countrycodes
import coordinates
from dotenv import load_dotenv
import pytz
import websockets

load_dotenv(".env")


async def connect_ais_stream():
    reset_color = "\033[0;0m"  # Resets formatting back to default

    async with websockets.connect(
        "wss://stream.aisstream.io/v0/stream"
    ) as websocket:
        subscribe_message = {
            "APIKey": os.getenv("AISSTREAM_API_KEY"),
            "BoundingBoxes": [coordinates.black_sea],
            "FilterMessageTypes": ["PositionReport"],
        }

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)

        async for message_json in websocket:
            message = json.loads(message_json)

            # Safely check if the incoming message is actually a PositionReport
            if message.get("MessageType") != "PositionReport":
                continue

            msg_data = message.get("Message", {})
            ais_message = msg_data.get("PositionReport")

            # Double check that PositionReport exists in payload
            if not ais_message:
                continue

            ais_name = message.get("MetaData", {})

            vessel_name = ais_name.get("ShipName", "Unknown").strip()
            current_time = datetime.now(pytz.timezone("Europe/Sofia"))
            ship_id = str(ais_message.get("UserID", "N/A"))
            lat = round(ais_message.get("Latitude", 0.0), 5)
            lon = round(ais_message.get("Longitude", 0.0), 5)

            country_code = ship_id[:3]  # Extracts first 3 digits from ship_id
            color = countrycodes.colors_dict.get(
                country_code, ""
            )  # Looks up color+country string

            log_str = f"[{current_time}] Name: {vessel_name} ShipId: {color} {ship_id}{reset_color} Latitude: {lat} Longitude: {lon}"

            print(
                f"[{current_time}]",
                f"Name: {vessel_name}",
                f"ShipId: {color} {ship_id}{reset_color}",
                f"Latitude: {lat} Longitude: {lon}",
            )

            # File is automatically closed when leaving the 'with' block
            with open("logs.txt", "a", encoding="utf-8") as f:
                f.write(log_str + "\n")


if __name__ == "__main__":
    asyncio.run(connect_ais_stream())