import anvil.server
from app_settings import AppSettings
from database import DataBase

config = AppSettings()

anvil.server.connect(config.anvil.uplink)


@anvil.server.callable
def get_event_data():
    data = []
    data = DataBase.read_from_db()
    return data


anvil.server.wait_forever()
