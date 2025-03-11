from pydantic import BaseModel, Field

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from database import create_connection, close_connection


info = Info(title="book API", version="1.0.0")
app = OpenAPI(__name__, info=info)


room_tag = Tag(name="room", description="Room")
device_tag = Tag(name="devices", description="Devices")
connection = create_connection()


class RoomRoute(BaseModel):
    rid: int = Field(..., title="Room ID", description="Room ID")

class Devices(BaseModel):
    Dvalue:int = Field(...,title="Devices Value", description="Devices Value")

class RoomControlDeviceRoute(BaseModel):
    rid: int = Field(..., title="Room ID", description="Room ID")
    did: int = Field(..., title="Device ID", description="Device ID")
    
@app.get("/room/<int:rid>", summary="get data from a specific room", tags=[room_tag])
def get_room(path: RoomRoute):
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
    return {
        "code": 0,
        "message": "ok",
        "data": {
            "id": str(path.rid)
        }
    }

@app.get("/room", summary="get all data from all rooms", tags=[room_tag])
def get_all_room():
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
    command = "SELECT SensorData.MeasurementID, SensorData.TimeStamp, SensorData.SensorType, SensorData.Value, RoomID, Room.Name, Room.Location FROM Room JOIN SensorData USING (RoomID) ORDER BY SensorData.MeasurementID;"
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
            "Name": row[5],
            "Location": row[6]
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

@app.post("/room/<int:rid>/device/<int:did>", summary="to controll a device", tags=[device_tag])
def controll_device(path: RoomControlDeviceRoute, body: Devices):
    """
    To controll a device in the room like 
    - Lights 
    - ... 
    """
    return {
        "value": 0,
        "": "ok",
        "data": {
            "id": str(path.rid)
        }
    }



                         
if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")

