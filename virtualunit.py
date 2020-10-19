import random
import paho.mqtt.publish as publish
# from app_settings import AppSettings

# config = AppSettings()


class VirtualUnit:
    Id = ""
    beaconId = ""
    rssi = 0
    beaconIds = []

    def generateRssi(self):
        rssi = random.randint(-80, -30)
        print(rssi)

    # def generateId():

    # def generateBeaconId():

    # def setInterval():

    # publish.single(config.mqttbroker.mqttusername + "/feeds/virtualunit", "heyload", hostname="io.adafruit.com",
    #                auth={'username': config.mqttbroker.mqttusername, 'password': config.mqttbroker.mqttpassword})

#     VirtualUnit
# const string Id;
# int payloadId;
# int rssi;
# const List<string> payloadIds;

# generaterssi()
# generateid()
# generatePayloadId()

# setInterval(int seconds)
# {
# publishTimer(seconds)
# timer.start()
# while timer.value < seconds
# generatePayloadId()
# generaterssi()
# client.Publish()
# }
