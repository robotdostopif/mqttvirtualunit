import anvil.server
import socket
import sys
import time

anvil.server.connect("752NKST3E7GZVBM2DAQZIFGR-DE3O5TTLAKIYPG2B")

total_received_data = []

@anvil.server.callable
def get_event_data():
    return total_received_data

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