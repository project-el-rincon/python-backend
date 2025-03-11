import json
import random
from paho.mqtt import client as mqtt_client


broker = '192.168.211.155'
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
        #### SQL Here ####
                
    for i in topics:
        client.subscribe(i)
    client.on_message = on_message


def publishControlAction(client, command, topic):
    result = client.publish(topic, str(command))
    if result[0] == 0:
        return True
    else:
        return False
    
client = connect_mqtt()

def run():
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
