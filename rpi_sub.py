"""
Team members: 
Brian Nlong Zhao, Weixuan Gao
"""

import paho.mqtt.client as mqtt
import sys
import time
from grovepi import *
# sys.path.append('../../Software/Python/')
import grovepi
import RPi.GPIO as GPIO

print("Enter a threshould value:")
th = input()
th = float(th)
t1 = 0
t2 = 0
t3 = 0
t4 = 0

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)

def on_C1(client, userdata, message):
    payload = str(message.payload, "utf-8")
    t1 = float(payload)
    print("Core 1 Temperature: " + payload + "℃ ", end=" ")
    if (t1 > th):
        GPIO.output(11, GPIO.HIGH)
        print("LED ON")
    else:
        GPIO.output(11, GPIO.LOW)
        print("LED OFF")

def on_C2(client, userdata, message):
    payload = str(message.payload, "utf-8")
    t2 = float(payload)
    print("Core 2 Temperature: " + payload + "℃ ", end=" ")
    if (t2 > th):
        GPIO.output(11, GPIO.HIGH)
        print("LED ON")
    else:
        GPIO.output(11, GPIO.LOW)
        print("LED OFF")

def on_C3(client, userdata, message):
    payload = str(message.payload, "utf-8")
    t3 = float(payload)
    print("Core 3 Temperature: " + payload + "℃ ", end=" ")
    if (t3 > th):
        GPIO.output(11, GPIO.HIGH)
        print("LED ON")
    else:
        GPIO.output(11, GPIO.LOW)
        print("LED OFF")

def on_C4(client, userdata, message):
    payload = str(message.payload, "utf-8")
    t4 = float(payload)
    print("Core 4 Temperature: " + payload + "℃ ", end=" ")
    if (t4 > th):
        GPIO.output(11, GPIO.HIGH)
        print(" LED ON")
    else:
        GPIO.output(11, GPIO.LOW)
        print(" LED OFF")

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))
    client.subscribe("briannlz/C1")
    client.subscribe("briannlz/C2")
    client.subscribe("briannlz/C3")
    client.subscribe("briannlz/C4")

def on_message(client, userdata, msg):
    client.message_callback_add("briannlz/C1", on_C1)
    client.message_callback_add("briannlz/C2", on_C2)
    client.message_callback_add("briannlz/C3", on_C3)
    client.message_callback_add("briannlz/C4", on_C4)

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="mqtt.eclipse.org", port=1883, keepalive=60)
    client.loop_start()

    while(True):
        time.sleep(0.1)