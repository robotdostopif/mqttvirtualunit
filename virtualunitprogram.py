from virtualunit import VirtualUnit
from app_settings import AppSettings
import logging

config = AppSettings()
mqttusername = config.mqttbroker.mqttusername
mqttpassword = config.mqttbroker.mqttpassword
mqttfeedpath = config.mqttbroker.mqttfeedpath


def start_units(amount):
    for i in range(amount):
        print(i)
        virtualunit = VirtualUnit(i + 1, mqttusername, mqttpassword,
                                  mqttfeedpath)
        virtualunit.start_unit()


try:
    rawAmount = input("Choose amount of Virtual Units to initlize: ")
    amount = int(rawAmount)
    while True:
        start_units(amount)
        print("Press Ctrl + C to Exit the simulation.")
except KeyboardInterrupt:
    pass
