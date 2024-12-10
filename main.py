from paho.mqtt import client as mqtt_client
import time

broker = "172.104.199.107"
port = 1883
topic = "1111111/#"
client_id = f'python_teste'
# username = 'emqx'
# password = 'public'

topic0 = "1111111/0/update"
topic2 = "1111111/2/update"
topic3 = "1111111/3/update"
topic4 = "1111111/4/update"


message0 = '0x5A00200400000000'
message_bytes0 = bytes.fromhex(message0[2:])  # b'Z\x07 \x03\x00\x00\x00\x00'

message = '0x5A02200400000000'
message_bytes = bytes.fromhex(message[2:])  # b'Z\x07 \x03\x00\x00\x00\x00'

def connect_mqtt():
    def on_connect(client, userdata, flags, reason_code, properties):
    # For paho-mqtt 2.0.0, you need to add the properties parameter.
    # def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # For paho-mqtt 2.0.0, you need to set callback_api_version.
    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)

    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, topic, msg):
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

def main():
    client = connect_mqtt()
    while True:
        publish(client, topic0, message_bytes0)
        publish(client, topic2, message_bytes)
        publish(client, topic3, message_bytes)
        publish(client, topic4, message_bytes)
        print("\n")
        time.sleep(30)

if __name__ == "__main__":
    main()