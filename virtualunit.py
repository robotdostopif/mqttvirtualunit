import random


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

    #

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
