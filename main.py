from typing import Optional
from pydantic import BaseModel, Field
import threading
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from database import create_connection, close_connection
import mqttHandler
import json

info = Info(title="book API", version="1.0.0")
app = OpenAPI(__name__, info=info)


room_tag = Tag(name="room", description="Room")
device_tag = Tag(name="devices", description="Devices")
connection = create_connection()


class RoomRoute(BaseModel):
    rid: str = Field(..., title="Room ID", description="Room ID")

class Data(BaseModel):
    sensorID: str = Field(...,title="SensorID", description="The ID of the sensor")
    topic: str = Field(...,title="topic", description="the MQTT Topic")
    value: float = Field(...,title="value", description="Value to change to")


class Devices(BaseModel):
    mqttTopic: str = Field(...,title="MQTT Topic", description="Enter the device type in a topic format (school/light)")
    command: Data = Field(..., title="ahbdabwd")

class TimestampQuery(BaseModel):
    from_timestamp: str = Field(None, title="From Timestamp", description="Start timestamp for the query (2021-01-01 00:00:00)")
    to_timestamp: str = Field(None, title="To Timestamp", description="End timestamp for the query (2021-01-01 00:00:00)")

class RoomControlDeviceRoute(BaseModel):
    did: int = Field(..., title="Device ID", description="Device ID")
    

class RoomData(BaseModel):
    MeasurementID: int = Field(..., title="Measurement ID")
    TimeStamp: str = Field(..., title="Timestamp")
    SensorType: str = Field(..., title="Sensor Type")
    Value: float = Field(..., title="Value")
    RoomID: Optional[int] = Field(None, title="Room ID")

class RoomResponse(BaseModel):
    code: int = Field(..., title="Response Code")
    message: str = Field(..., title="Response Message")
    data: list[RoomData] = Field(..., title="Room Data")

@app.get("/room/<string:rid>", summary="get data from a specific room", tags=[room_tag], responses={200: RoomResponse})
def get_room(path: RoomRoute, query: TimestampQuery) -> RoomResponse:
    """
    Get date from a specific room like 
    - Energy usage
    - Temperature
    - Humidity
    - Lights
    - Co2 level
    - Volume
    - If ther is Motion in the room

    """
    command = f"SELECT id, sensorroom, timestamp, sensortype, value FROM Measurement WHERE sensorroom = '{path.rid}'"
    if query.from_timestamp and query.to_timestamp:
        command += f" AND timestamp BETWEEN '{query.from_timestamp}' AND '{query.to_timestamp}'"
    if(query.from_timestamp and not query.to_timestamp):
        command += f" AND timestamp > '{query.from_timestamp}'"
    if(not query.from_timestamp and query.to_timestamp):
        command += f" AND timestamp < '{query.to_timestamp}'" 
    print(command)
    cursor = connection.cursor()
    cursor.execute(command)
    data = cursor.fetchall()
    handled_data = []
    for row in data:
        room_id = row[4]
        room_data = {
            "MeasurementID": row[0],
            "TimeStamp": row[1],
            "SensorType": row[2],
            "Value": row[3],
            "RoomID": row[4],
        }
        room_found = next((item for item in handled_data if item["roomid"] == room_id), None)
        if room_found:
            room_found["data"].append(room_data)
        else:
            handled_data.append({"roomid": room_id, "data": [room_data]})
        data = handled_data
    return {
        "code": 0,
        "message": "ok",
        "data": data
    }

@app.get("/room", summary="get all data from all rooms", tags=[room_tag], responses={200: RoomResponse})
def get_all_room(query: TimestampQuery) -> RoomResponse:
    """
    Get the data from all the rooms 
    - Energy usage
    - Temperature
    - Humidity
    - Lights
    - Co2 level
    - Volume
    - If ther is Motion in the room
    """
    command = f"SELECT id, sensorroom, timestamp, sensortype, value FROM Measurement "
    if query.from_timestamp and query.to_timestamp:
        command += f" WHERE timestamp BETWEEN '{query.from_timestamp}' AND '{query.to_timestamp}'"
    if(query.from_timestamp and not query.to_timestamp):
        command += f" WHERE timestamp > '{query.from_timestamp}'"
    if(not query.from_timestamp and query.to_timestamp):
        command += f" WHERE timestamp < '{query.to_timestamp}'" 
    cursor = connection.cursor()
    cursor.execute(command)
    data = cursor.fetchall()
    handled_data = []
    for row in data:
        room_id = row[1]
        room_data = {
            "MeasurementID": row[0],
            "TimeStamp": row[2],
            "SensorType": row[3],
            "Value": row[4]
        }
        room_found = next((item for item in handled_data if item["roomid"] == room_id), None)
        if room_found:
            room_found["data"].append(room_data)
        else:
            handled_data.append({"roomid": room_id, "data": [room_data]})
    data = handled_data
    return {
        "code": 0,
        "message": "ok",
        "data": data
    }

@app.post("/device", summary="to control a device", tags=[device_tag])
def controll_device(body: Data):
    """
    To controll a device in the room like 
    - Lights 
    - ... 


    Valid Topics: ["school/energy", "school/temperature", "school/humidity", "school/light", "school/co2", "school/volume", "school/motion", "school/tvoc"]
    """
    jstring = {
        "sensorID":body.sensorID,
        "topic":body.topic,
        "value":body.value
    }
    mqttHandler.publishControlAction(mqttHandler.client, json.dumps(jstring), body.topic)
    return {}



                         
if __name__ == "__main__":
    def mqttThread():
        mqttHandler.run()
    x = threading.Thread(target=mqttThread)
    x.start()
    app.run(debug=False, port=5001, host="0.0.0.0")

