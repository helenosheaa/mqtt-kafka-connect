import paho.mqtt.client as mqtt
from random import uniform
import time

mqtt_broker = 'mqtt.eclipseprojects.io'
mqtt_client = mqtt.Client('MQTTProducer')
mqtt_client.connect(mqtt_broker)


while True:
    randNumber = uniform(20.0, 21.0)
    mqtt_client.publish("temperature3", randNumber)
    print('MQTT: Just published ' + str(randNumber) + 'to topic temperature3')
    time.sleep(3)