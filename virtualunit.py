import paho.mqtt.publish as publish
from app_settings import AppSettings

config = AppSettings()
publish.single(config.mqttbroker.mqttusername + "/feeds/virtualunit", "hayload", hostname="io.adafruit.com",
               auth={'username': config.mqttbroker.mqttusername , 'password': config.mqttbroker.mqttpassword })
