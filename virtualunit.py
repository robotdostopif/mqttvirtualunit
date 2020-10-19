import random
import yaml
import os
import time
import paho.mqtt.publish as publish


class VirtualUnit:
    recieverId = ""
    mqttusername = ""
    mqttpassword = ""
    mqttfeedpath = ""
    beaconId = ""
    rssi = 0

    def __init__(self, recieverId, mqttusername, mqttpassword, mqttfeedpath):
        self.recieverId = recieverId
        self.mqttusername = mqttusername
        self.mqttpassword = mqttpassword
        self.mqttfeedpath = mqttfeedpath
        self.beaconId = self.generateBeaconId()
        self.rssi = self.generateRssi()

    def generateRssi(self):
        return random.randint(-80, -30)

    def generateBeaconId(self):
        yaml_file = open("config/beacons.yaml")
        parsed_yaml_file = yaml.load(yaml_file, Loader=yaml.FullLoader)
        beaconIds = parsed_yaml_file.get("beaconids")
        return random.choice(beaconIds)

    def publish_message(self, message):
        publish.single(self.mqttusername + "/feeds/" + self.mqttfeedpath, message, hostname="io.adafruit.com", client_id=str(self.recieverId),
                       auth={'username': self.mqttusername, 'password': self.mqttpassword})
        print(message)

    def start_unit(self):
        time.sleep(random.randint(1, 5))
        payload = self.beaconId + " " + str(self.rssi)
        self.publish_message(payload)
