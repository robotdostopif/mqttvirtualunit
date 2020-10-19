from virtualunit import VirtualUnit
from app_settings import AppSettings

config = AppSettings()
mqttusername = config.mqttbroker.mqttusername 
mqttpassword = config.mqttbroker.mqttpassword
print(mqttusername)
print(mqttpassword)
def start_units(amount):
    for i in range(amount):
        print(i)
        virtualunit = VirtualUnit(amount+1,mqttusername,mqttpassword)
        virtualunit.start_unit()

def main():
    amount = input("Choose amount of Virtual Units to initlize: ") 
    start_units(amount)
    print("Press Ctrl + C to Exit the simulation.")

main()