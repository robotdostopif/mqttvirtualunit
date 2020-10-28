import unittest
from virtualunit import VirtualUnit


class VirtualUnitTest(unittest.TestCase):
    def test_generate_beaconid(self):
        recieverId = 1
        mqttusername = ""
        mqttpassword = ""
        mqttfeedpath = ""
        virtualunit = VirtualUnit(1, mqttusername, mqttpassword, mqttfeedpath)
        beaconId = virtualunit.generateBeaconId()
        self.assertTrue(beaconId)

    def test_generate_rssi(self):
        recieverId = 1
        mqttusername = ""
        mqttpassword = ""
        mqttfeedpath = ""
        virtualunit = VirtualUnit(1, mqttusername, mqttpassword, mqttfeedpath)
        rssi = virtualunit.generateRssi()
        self.assertTrue(rssi)
