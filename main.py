import os, json, schedule, time, threading
from sqlCommand import Command
from dotenv import load_dotenv
from threading import Thread
from serverSocket import ServerSocket
from synchronizing import DataSync

class startServer(ServerSocket, DataSync, Command):
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    def __init__(self):
        self.acceptData = {}
        self.dats = False
        self.otvet = {}
        self.govno = 1
        self.spisokDlyaSravneniya = []
        self.spisokDlyaSravneniyaDva = []
        self.spisokDlyaSravneniyaTri = []
        self.spisokDlyaSravneniyaChet = []
        self.contactMySQL = 0
        self.checkStatus = 0
        super().CommandSQL()
        self.checkSocket()
        self.checkSchedule()
        # self.connect()



    def scheduleTask(self):
        schedule.every(10).seconds.do(self.request).tag('Task')
        # schedule.every(10).seconds.do(self.startMysql).tag('Task')
        while True:
            if self.checkStatus == 0:
                schedule.run_pending()
                time.sleep(1)
            else:
                break

    def request(self):
        self.otvet = self.acceptRequests()
        base = {"1": {"login": "admin", "loginAPI": "admin", "time": "2022.10.05.10.10.10",
                         "text": {"notifications":'meeting', 'descriptions':'123qweasd', 'url':'urls'}}}
        if self.dats:
            raw_data = json.dumps(base)
            self.connection.sendall(raw_data.encode("utf-8"))
        # elif self.client_address:
        #     print('Нет данных от:', self.client_address)
        else:
            pass
        self.dats = False

    def transformation(self):
        transformLogin = self.acceptData["login"]
        transformLoginAPI = self.acceptData["loginAPI"]
        return
        # self.acceptData

    def Collec(self):
        schedule.every(10).seconds.do(self.connServer).tag('Conn')
        # schedule.every(10).seconds.do(self.startMysql).tag('Task')
        while True:
            if self.checkStatus == 0:
                schedule.run_pending()
                time.sleep(1)
            else:
                break

    def connServer(self):
        lol = ServerSocket()
        lol.conn()
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
            # self.lcs = Thread(target=ServerSocket)
            self.lcs = Thread(target=self.Collec)
            # self.lcs.start()
            self.lcs.start()
        finally:
            lockCheckSocket.release()

    def checkSchedule(self):
        lockCheckSocket = threading.Lock()
        lockCheckSocket.acquire()
        try:
            self.lcs = Thread(target=self.scheduleTask)
            self.lcs.start()
        finally:
            lockCheckSocket.release()


    def startSocket(self):
        pass

    def recordsLogs(self):
        pass

if __name__=="__main__":
    start = startServer()
    # starte.connect()