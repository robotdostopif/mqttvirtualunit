from virtualunit import VirtualUnit
from app_settings import AppSettings
import paho.mqtt.publish as publish

config = AppSettings()
mqqtusername = config.mqttbroker.mqttusername 
mqttpassword = config.mqttbroker.mqttpassword

vu = VirtualUnit()
vu.generateRssi()

def publish(mqttusername, mqttpassword, message):
    publish.single(mqttusername + "/feeds/virtualunit", message, hostname="io.adafruit.com",
                    auth={'username': mqttusername, 'password': mqttpassword})