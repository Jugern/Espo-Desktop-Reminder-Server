import serverSocket
import os, json
from dotenv import load_dotenv
from threading import Thread

class start(serverSocket.ServerSocket):
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    def __init__(self):
        self.acceptData = {}
        super().__init__()
        # self.connect()

    def request(self, dats=False):
        base = {"1": {"login": "admin", "loginAPI": "admin", "time": "2022.10.05.10.10.10",
                         "text": {"notifications":'meeting', 'descriptions':'123qweasd', 'url':'urls'}}}
        if dats:
            raw_data = json.dumps(base)
            self.connection.sendall(raw_data.encode("utf-8"))
        else:
            print('Нет данных от:', self.client_address)

    def transformation(self):
        transformLogin = self.acceptData["login"]
        transformLoginAPI = self.acceptData["loginAPI"]
        print(transformLogin)
        print(transformLoginAPI)
        return
        # self.acceptData

    def acceptRequests(self):
        pass

    def sendAReply(self):
        pass

    def databaseSync(self):
        pass
    
    def checkSocket(self):
        lockCheckSocket = threading.Lock()
        lockCheckSocket.acquire()
        try:
            self.lcs = Thread(target=serverSocket.ServerSocket)
            self.lcs.start()
        finally:
            lockCheckSocket.release()

    def startSocket(self):
        pass

    def recordsLogs(self):
        pass

if __name__=="__main__":
    start = start()
    # starte.connect()