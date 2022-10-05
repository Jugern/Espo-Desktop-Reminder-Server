import socket
import json
import os
from dotenv import load_dotenv

class ServerSocket():
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (os.environ.get('host'), int(os.environ.get('port')))
        print('Подключен к ip {} порт {}'.format(*self.server_address))

    def request(self, connection, client_address, dats=False):
        # base = {'da': 12}
        base = {"1": {"login": "admin", "loginAPI": "12345678", "time": "2022.10.05.10.10.10",
                         "text": {"notifications":'call', 'url':'urls'}}}
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

    # def checkSocket(self):


connect = ServerSocket()
connect.connect()