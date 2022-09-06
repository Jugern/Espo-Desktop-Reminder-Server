import socket
# import sys
import json

def request(connection, client_address, dats=False):
    # base = {'da': 12}
    base = {"data":{"hostname":"192.168.7.6","ipaddress":"192.168.7.6","comment":"АдминистраторСервер", "command":"discovery"}}
    if dats:
        raw_data = json.dumps(base)
        connection.sendall(raw_data.encode("utf-8"))
    else:
        print('Нет данных от:', client_address)

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 19000)
    # print('Старт сервера на {} порт {}'.format(*server_address))
    sock.bind(server_address)
    sock.listen(20)
    while True:
        connection, client_address = sock.accept()
        # print(1)
        try:
            data = connection.recv(1024)
            if data.decode() == False:
                print(data.decode())
            if data.decode():
                dats = json.loads(data)
                print(dats)
            if dats:
                request(connection, client_address, True)
        except socket.error as errorSocket:
            print(errorSocket)
        finally:
            connection.close()
connect()