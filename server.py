import anvil.server
import socket
import sys
import time
import pyodbc
import json
import datetime
from app_settings import AppSettings

config = AppSettings()
anvil.server.connect(config.anvil.uplink)
server = config.sqlconnection.sqlserver
database = config.sqlconnection.sqldatabase
driver = config.sqlconnection.sqldriver
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
def get_reference_data(beaconID):
    file = open('config/assetreference.json')
    data = json.load(file)
    for d in data:
        if d['beaconId'] == beaconID:
            file.close()
            return d
@anvil.server.callable
def get_event_data():
    data = []
    dbCall = pyodbc.connect('Driver='+driver+'; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;')
    with dbCall.cursor() as cur:
        cur.execute('SELECT * FROM Events')
        rows = cur.fetchall()
        for row in rows:
            refData = get_reference_data(row[3])
            print(refData)
            data.append({'description':refData['description'],'id': row[0], 'type': row[1], 'recieverId' :row[2], 'beaconId' :row[3], 'rssi':row[4]})
        return data

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_name = 'localhost'   # user sys.argv[1] to bind the socket to the address given on the command line
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)
sock.listen(1)
get_reference_data('5adb6608-1171-4d8c-a3fc-50e2e645ea81')
while True:             # instead of anvil.server.run_forever()
    time.sleep(1)
    print('waiting for a connection', file=sys.stderr)
    connection, client_address = sock.accept()
    try:
        print('client connected:', client_address, file=sys.stderr)
        total_received_data = []
        while True:
            data = connection.recv(16)
            print('received "%s"' % data, file=sys.stderr)
            if data:
                total_received_data += data
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()