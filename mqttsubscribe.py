import datetime
import pyodbc
import json
import paho.mqtt.client as paho
from app_settings import AppSettings

config = AppSettings()
server = config.sqlconnection.sqlserver
database = config.sqlconnection.sqldatabase
driver = config.sqlconnection.sqldriver
def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_message(client, userdata, msg):
    add_message_to_database(msg)
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    

client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
username_pw_set(config.mqttbroker.mqttusername, password=config.mqttbroker.mqttpassword)
client.connect(“io.adafruit.com”, 1883)
client.subscribe(“config.mqttusername + "/feeds/" + config.mqttfeedpath, qos=1)

client.loop_forever()

    
def add_message_to_database(messagesObj):
    dbCall = pyodbc.connect('Driver='+driver+'; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;')
    cursor = dbCall.cursor()
    sql = "INSERT INTO Events (RecieverId, BeaconId, Rssi, Created) VALUES (?, ?, ?, ?)"
    val = (messagesObj['RecieverId'], messagesObj['BeaconId'], messagesObj['Rssi'], datetime.datetime.now())
    cursor.execute(sql,val)
    dbCall.commit()