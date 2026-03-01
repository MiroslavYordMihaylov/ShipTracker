import asyncio
import pytz
import websockets
import json
from datetime import datetime, timezone
import art
import countrycodes

async def connect_ais_stream():

    print(art.caption)
    print(art.ship)

    reset_color = "\033[0;0m"  # Resets formatting back to default

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        # "FiltersShipMMSI": ["538007480", "636015988", "316003701"]
        subscribe_message = {"APIKey": "7d90db489d07087e49b22d9cda307bbe4c0dac77",
                             "BoundingBoxes": [[[40.9, 27.45], [46.6, 41.77]]],
                             "FilterMessageTypes": ["PositionReport"]
                             }

        subscribe_message_json = json.dumps(subscribe_message)
        await websocket.send(subscribe_message_json)

        async for message_json in websocket:
            message = json.loads(message_json)
            ais_message = message['Message']['PositionReport']
            ais_name = message['MetaData']

            vessel_name = ais_name['ShipName']
            current_time =datetime.now(pytz.timezone('Europe/Sofia'))
            ship_id = str(ais_message['UserID'])
            lat = round(ais_message['Latitude'], 5)
            lon = round(ais_message['Longitude'], 5)

            country_code = ship_id[:3]  # Extracts first 3 digits from ship_id
            color = countrycodes.colors_dict.get(country_code, '')  # Looks up the color+country string

            print(f"[{current_time}]",f"Name: {vessel_name.strip()}", f"ShipId: {color} {ship_id}{reset_color}", f"Latitude: {lat} Longitude: {lon}")

if __name__ == "__main__":
    asyncio.run(connect_ais_stream())