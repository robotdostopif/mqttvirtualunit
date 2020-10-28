import anvil
import anvil.server
import socket
import sys
import time
import pyodbc
import json
import datetime
from app_settings import AppSettings
from database import DataBase

config = AppSettings()
anvil.server.connect(config.anvil.uplink)
server = config.sqlconnection.sqlserver
database = config.sqlconnection.sqldatabase
driver = config.sqlconnection.sqldriver


@anvil.server.callable
def get_event_data():
    data = []
    data = DataBase.read_from_db()
    return data


anvil.server.wait_forever()
