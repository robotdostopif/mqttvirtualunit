import pyodbc
import anvil
import json
import datetime
from app_settings import AppSettings

config = AppSettings()
server = config.sqlconnection.sqlserver
database = config.sqlconnection.sqldatabase
driver = config.sqlconnection.sqldriver


class DataBase:
    def read_from_db():
        data = []
        dbCall = pyodbc.connect('Driver=' + driver + '; SERVER=' + server +
                                '; DATABASE=' + database +
                                '; Trusted_Connection=True;')
        with dbCall.cursor() as cur:
            cur.execute('SELECT * FROM Events')
            rows = cur.fetchall()
            print(rows)
            for row in rows:
                refData = get_reference_data(row[2])
                print(refData)
                data.append({
                    'description': refData['description'],
                    'id': row[0],
                    'type': refData['type'],
                    'recieverId': row[1],
                    'beaconId': row[2],
                    'rssi': row[3],
                    'created': row[4]
                })
        return data

    def write_to_db(messagesObj):
        dbCall = pyodbc.connect('Driver=' + driver + '; SERVER=' + server +
                                '; DATABASE=' + database +
                                '; Trusted_Connection=True;')
        cursor = dbCall.cursor()
        sql = "INSERT INTO Events (RecieverId, BeaconId, Rssi, Created) VALUES (?, ?, ?, ?)"
        val = (messagesObj['RecieverId'], messagesObj['BeaconId'],
               messagesObj['Rssi'], datetime.datetime.now())
        cursor.execute(sql, val)
        dbCall.commit()

    def get_reference_data(beaconID):
        file = open('config/assetreference.json')
        data = json.load(file)
        for d in data:
            if d['beaconId'] == beaconID:
                file.close()
                return d
