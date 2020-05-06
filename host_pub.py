"""
Team members: 
Brian Nlong Zhao, Weixuan Gao
"""

import wmi
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))

def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + "/" + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host="mqtt.eclipse.org", port=1883, keepalive=60)
    while True:
        time.sleep(1)
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature':
                print(sensor.Name)
                print(sensor.Value)
                if sensor.Name == "CPU Core #1":
                    client.publish("briannlz/C1", str(sensor.Value))
                if sensor.Name == "CPU Core #2":
                    client.publish("briannlz/C2", str(sensor.Value))
                if sensor.Name == "CPU Core #3":
                    client.publish("briannlz/C3", str(sensor.Value))
                if sensor.Name == "CPU Core #4":
                    client.publish("briannlz/C4", str(sensor.Value))