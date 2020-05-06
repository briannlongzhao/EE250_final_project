"""
Team members: 
Brian Nlong Zhao, Weixuan Gao
"""

import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import time

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []

fig, axs = plt.subplots(2, 2, sharex='col', sharey='row')
fig.suptitle("CPU Temperature on Host Laptop")
    

def on_C1(client, userdata, message):
    payload = str(message.payload, "utf-8")
    x1.append(dt.datetime.now().strftime('%H:%M:%S'))
    y1.append(float(payload))
    print("Core 1 Temperature: " + payload + "℃")

def on_C2(client, userdata, message):
    payload = str(message.payload, "utf-8")
    x2.append(dt.datetime.now().strftime('%H:%M:%S'))
    y2.append(float(payload))
    print("Core 2 Temperature: " + payload + "℃")
    
def on_C3(client, userdata, message):
    payload = str(message.payload, "utf-8")
    x3.append(dt.datetime.now().strftime('%H:%M:%S'))
    y3.append(float(payload))
    print("Core 3 Temperature: " + payload + "℃")

def on_C4(client, userdata, message):
    payload = str(message.payload, "utf-8")
    x4.append(dt.datetime.now().strftime('%H:%M:%S'))
    y4.append(float(payload))
    print("Core 4 Temperature: " + payload + "℃")

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

def animate(i, x1, y1, x2, y2, x3, y3, x4, y4):
    x1 = x1[-10:]
    y1 = y1[-10:]
    x2 = x2[-10:]
    y2 = y2[-10:]
    x3 = x3[-10:]
    y3 = y3[-10:]
    x4 = x4[-10:]
    y4 = y4[-10:]

    axs[0,0].clear()
    axs[0,0].plot(x1, y1)
    axs[0,0].set_title('Core 1')
    axs[0,1].clear()
    axs[0,1].plot(x2, y2, 'tab:orange')
    axs[0,1].set_title('Core 2')
    axs[1,0].clear()
    axs[1,0].plot(x3, y3, 'tab:green')
    axs[1,0].set_title('Core 3')
    axs[1,1].clear()
    axs[1,1].plot(x3, y4, 'tab:red')
    axs[1,1].set_title('Core 4')

    for ax in axs.flat:
        ax.set(xlabel='Time', ylabel='Temperature (℃)')
        ax.label_outer()

    plt.subplots_adjust(bottom=0.20)
    axs[1,0].tick_params('x', labelrotation=45)
    axs[1,1].tick_params('x', labelrotation=45)

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="mqtt.eclipse.org", port=1883, keepalive=60)
    client.loop_start()

    ani = animation.FuncAnimation(fig, animate, fargs=(x1,y1,x2,y2,x3,y3,x4,y4), interval=1000)
    plt.show()
