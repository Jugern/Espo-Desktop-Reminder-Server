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
        self.sock.bind(self.server_address)
        self.sock.listen(20)
        print('loh')

    def conn(self):
        while True:
            self.connection, self.client_address = self.sock.accept()
            try:
                data = self.connection.recv(1024)
                if data.decode() == False:
                    print(data.decode())
                try:
                    if data.decode():
                        dats = json.loads(data)
                except json.decoder.JSONDecodeError as jsonError:
                    print(jsonError)
                # print(dats)
                # self.dats = True
                # self.acceptData = dats
                # if dats:
                # self.transformation()
                # self.request(True)
            except socket.error as errorSocket:
                print(errorSocket)
            finally:
                self.connection.close()

