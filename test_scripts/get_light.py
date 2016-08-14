#!/usr/bin/python

import paho.mqtt.client as paho
mqttc = paho.Client()
topic = "mbed/request/endpoints/cc69e7c5-c24f-43cf-8365-8d23bb01c707/311/0/5850"
message = "{\"path\":\"/311/0/5850\",\"ep\":\"cc69e7c5-c24f-43cf-8365-8d23bb01c707\",\"coap_verb\":\"get\"}"
ip = "192.168.1.213"
mqttc.connect(ip, 1883, 60)
mqttc.publish(topic,message)
mqttc.disconnect();
