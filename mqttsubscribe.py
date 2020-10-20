import paho.mqtt.subscribe as subscribe
import datetime
import pyodbc
import json
from collections import namedtuple
from json import JSONEncoder
from app_settings import AppSettings

config = AppSettings()
mqttusername = config.mqttbroker.mqttusername
mqttpassword = config.mqttbroker.mqttpassword
mqttfeedpath = config.mqttbroker.mqttfeedpath
driver = "Driver={SQL Server};"
server = "DESKTOP-2IS2C3L\SQLEXPRESS" 
database = "EventDB" 

# def customEventDecoder(selfeventDict):
#     # return namedtuple('X', eventDict.keys())(*str(eventDict.values()))
#     return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)

def subscribe_message():
    messagesJson = subscribe.simple(mqttusername + "/feeds/" + mqttfeedpath, hostname="io.adafruit.com",
                       auth={'username': mqttusername, 'password': mqttpassword})
    messagesObj = json.loads(messagesJson.payload)
    print(messagesObj)
    dbCall = pyodbc.connect('Driver={SQL Server}; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;')
    cursor = dbCall.cursor()
    sql = "INSERT INTO Events (AssetType, RecieverId, BeaconId, Rssi, Created) VALUES (?, ?, ?, ?, ?)"
    val = ("person", messagesObj['RecieverId'], messagesObj['BeaconId'], messagesObj['Rssi'], datetime.datetime.now())
    cursor.execute(sql,val)
    dbCall.commit()

def main():
    try:
        while True:
            subscribe_message()
            print("Press Ctrl + C to Exit to stop subscribe.")
    except KeyboardInterrupt:
        pass

main()
