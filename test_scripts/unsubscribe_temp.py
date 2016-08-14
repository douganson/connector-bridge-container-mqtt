#!/usr/bin/python

import paho.mqtt.client as paho
mqttc = paho.Client()
topic = "mbed/request/subscriptions/endpoints/cc69e7c5-c24f-43cf-8365-8d23bb01c707/303/0/5700"
message = "{\"path\":\"/303/0/5700\",\"ep\":\"cc69e7c5-c24f-43cf-8365-8d23bb01c707\",\"ept\":\"mbed-endpoint\",\"verb\":\"unsubscribe\"}"
ip = "192.168.1.213"
mqttc.connect(ip, 1883, 60)
mqttc.publish(topic,message)
mqttc.disconnect();
