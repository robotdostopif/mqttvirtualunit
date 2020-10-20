import anvil.server
import socket
import sys
import time
import pyodbc
import json
import datetime
from app_settings import AppSettings

anvil.server.connect("JHNUAAIPIVCORMAII7AEP2IE-B5DR34S2FJJZIT3R")
config = AppSettings()
server = config.sqlconnection.sqlserver
database = config.sqlconnection.sqldatabase
driver = config.sqlconnection.sqldriver
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@anvil.server.callable
def get_event_data():
    data = []
    dbCall = pyodbc.connect('Driver='+driver+'; SERVER='+server+'; DATABASE='+database+'; Trusted_Connection=True;')
    cursor = dbCall.cursor()
    cursor.execute('SELECT * FROM Events')
    rows = cursor.fetchall()
    for row in rows:
        data.append(list(row))
    return json.dumps(data, default = myconverter)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_name = 'localhost'   # user sys.argv[1] to bind the socket to the address given on the command line
server_address = (server_name, 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)
sock.listen(1)

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