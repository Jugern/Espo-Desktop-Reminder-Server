import socket
# import sys
import json

class ServerSocket():

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('localhost', 19000)
        print('Подключен к ip {} порт {}'.format(*self.server_address))

    def request(self, connection, client_address, dats=False):
        # base = {'da': 12}
        base = {"data": {"hostname": "192.168.7.6", "ipaddress": "192.168.7.6", "comment": "АдминистраторСервер",
                         "command": "discovery"}}
        if dats:
            raw_data = json.dumps(base)
            connection.sendall(raw_data.encode("utf-8"))
        else:
            print('Нет данных от:', client_address)

    def connect(self):
        # print('Старт сервера на {} порт {}'.format(*server_address))
        self.sock.bind(self.server_address)
        self.sock.listen(20)
        while True:
            self.connection, self.client_address = self.sock.accept()
            # print(1)
            try:
                data = self.connection.recv(1024)
                if data.decode() == False:
                    print(data.decode())
                if data.decode():
                    dats = json.loads(data)
                    print(dats)
                if dats:
                    self.request(self.connection, self.client_address, True)
            except socket.error as errorSocket:
                print(errorSocket)
            finally:
                self.connection.close()


connect = ServerSocket()
connect.connect()