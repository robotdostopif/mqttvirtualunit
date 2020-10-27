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
    def get_reference_data(beaconID):
        try:
            file = open("config/assetreference.json")
            data = json.load(file)
            for d in data:
                if d["beaconId"] == beaconID:
                    file.close()
                    return d
        except ValueError:
            print("Decoding JSON has failed.")

    def read_from_db():
        try:
            data = []
            dbCall = pyodbc.connect(
                "Driver="
                + driver
                + "; SERVER="
                + server
                + "; DATABASE="
                + database
                + "; Trusted_Connection=True;"
            )
            with dbCall.cursor() as cur:
                cur.execute("SELECT * FROM Events")
                rows = cur.fetchall()
                # print(rows)
                for row in rows:
                    refData = DataBase.get_reference_data(row[2])
                    # print(refData)
                    data.append(
                        {
                            "description": refData["description"],
                            "id": row[0],
                            "type": refData["type"],
                            "recieverId": row[1],
                            "beaconId": row[2],
                            "rssi": row[3],
                            "measuredpower": row[4],
                            "created": row[5],
                        }
                    )
                return data
        except pyodbc.DatabaseError as err:
            print(err)
            print("hello")
            raise err

    def write_to_db(messagesObj):
        try:
            dbCall = pyodbc.connect(
                "Driver="
                + driver
                + "; SERVER="
                + server
                + "; DATABASE="
                + database
                + "; Trusted_Connection=True;"
            )
            cursor = dbCall.cursor()
            sql = "INSERT INTO Events (ReceiverId, BeaconId, Rssi, MeasuredPower, Created) VALUES (?, ?, ?, ?, ?)"
            val = (
                messagesObj["RecieverId"],
                messagesObj["BeaconId"],
                messagesObj["Rssi"],
                messagesObj["MeasuredPower"],
                datetime.datetime.now(),
            )
            cursor.execute(sql, val)
            dbCall.commit()
        except pyodbc.DatabaseError as err:
            raise err
