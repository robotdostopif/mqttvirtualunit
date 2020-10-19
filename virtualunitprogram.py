from virtualunit import VirtualUnit
from app_settings import AppSettings

config = AppSettings()
mqttusername = config.mqttbroker.mqttusername
mqttpassword = config.mqttbroker.mqttpassword
mqttfeedpath = config.mqttbroker.mqttfeedpath
print(mqttusername)
print(mqttpassword)


def start_units(amount):
    for i in range(amount):
        print(i)
        virtualunit = VirtualUnit(
            amount+1, mqttusername, mqttpassword, mqttfeedpath)
        virtualunit.start_unit()


def main():
    try:
        rawAmount = input("Choose amount of Virtual Units to initlize: ")
        amount = int(rawAmount)
        while True:
            start_units(amount)
            print("Press Ctrl + C to Exit the simulation.")
    except KeyboardInterrupt:
        pass


main()
