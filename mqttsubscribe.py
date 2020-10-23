import paho.mqtt.subscribe as subscribe
import datetime
import pyodbc
import json
from app_settings import AppSettings
from database import DataBase

config = AppSettings()
mqttusername = config.mqttbroker.mqttusername
mqttpassword = config.mqttbroker.mqttpassword
mqttfeedpath = config.mqttbroker.mqttfeedpath
server = config.sqlconnection.sqlserver
database = config.sqlconnection.sqldatabase
driver = config.sqlconnection.sqldriver


def subscribe_message():
    messagesJson = subscribe.simple(mqttusername + "/feeds/" + mqttfeedpath,
                                    hostname="io.adafruit.com",
                                    auth={
                                        'username': mqttusername,
                                        'password': mqttpassword
                                    })
    messagesObj = json.loads(messagesJson.payload)
    print(messagesObj)
    DataBase.write_to_db(messagesObj)


def main():
    try:
        while True:
            subscribe_message()
            print("Press Ctrl + C to Exit to stop subscribe.")
    except KeyboardInterrupt:
        pass


main()
