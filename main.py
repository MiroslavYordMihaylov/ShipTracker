import asyncio
import pytz
import websockets
import json
from datetime import datetime, timezone

import art


async def connect_ais_stream():

    print(art.caption)
    print(art.ship)

    async with websockets.connect("wss://stream.aisstream.io/v0/stream") as websocket:
        # "FiltersShipMMSI": ["538007480", "636015988", "316003701"]
        subscribe_message = {"APIKey": "<YOUR API KEY>",
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

            if(ship_id.startswith('207')):
                print(f"[{current_time}]",f"Name: {vessel_name}", f"ShipId:\033[92m BG {ship_id}\033[0;0m", f"Latitude: {lat} Longitude: {lon}")
            elif (ship_id.startswith('271')):
                print(f"[{current_time}]",f"Name: {vessel_name}", f"ShipId:\033[91m TR {ship_id}\033[0;0m", f"Latitude: {lat} Longitude: {lon}")
            elif (ship_id.startswith('213')):
                print(f"[{current_time}]",f"Name: {vessel_name}", f"ShipId: GE {ship_id}", f"Latitude: {lat} Longitude: {lon}")
            elif (ship_id.startswith('273')):
                print(f"[{current_time}]",f"Name: {vessel_name}", f"ShipId:\033[94m RU {ship_id}\033[0;0m", f"Latitude: {lat} Longitude: {lon}")
            elif (ship_id.startswith('272')):
                print(f"[{current_time}]",f"Name: {vessel_name}", f"ShipId:\033[93m UA {ship_id}\033[0;0m", f"Latitude: {lat} Longitude: {lon}")
            else:
                print(f"[{current_time}]",f"Name: {vessel_name}", f"ShipId: {ship_id}", f"Latitude: {lat} Longitude: {lon}")


if __name__ == "__main__":
    asyncio.run(connect_ais_stream())
