import json
import random
from paho.mqtt import client as mqtt_client
import database

conn = database.create_connection()
broker = '192.168.0.52'
port = 1883
# topic = "school/energy"
topics = ["school/energy", "school/temperature", "school/humidity", "school/light", "school/co2", "school/volume", "school/motion", "school/tvoc"]
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        data = json.loads(msg.payload.decode())
        database.execute_command_with_write(conn, f"""INSERT INTO "Measurement" VALUES ('{data["location"]}','{data["timestamp"]}','{msg.topic}',{data["value"]});""")
        #### SQL Here ####
    for topic in topics:
        print(topic)
        client.subscribe(topic, qos=0)
    client.on_message = on_message


def publishControlAction(clienta, command, topic):
    result = clienta.publish(topic, str(command), qos=0)
    if result[0] == 0:
        return True
    else:
        return False
    
client = connect_mqtt()

def run():
    subscribe(client)
    client.loop_forever()



