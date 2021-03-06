import datetime
import pyodbc
import json
import paho.mqtt.client as paho
import log
from app_settings import AppSettings
from database import DataBase

config = AppSettings()
logger = log.get_logger("mqtt")


def on_subscribe(client, userdata, mid, granted_qos):
    logger.info("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    logger.info(string)


def on_message(client, userdata, msg):
    messagesObj = json.loads(msg.payload)
    DataBase.write_to_db(messagesObj)
    logger.info(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client()
client.username_pw_set(
    config.mqttbroker.mqttusername, password=config.mqttbroker.mqttpassword
)
client.connect("io.adafruit.com", 1883)
client.subscribe(
    config.mqttbroker.mqttusername + "/feeds/" + config.mqttbroker.mqttfeedpath, qos=1
)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_log = on_log

while True:
    try:
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
        exit(0)
    except:
        raise
