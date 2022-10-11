import serverSocket
# import os
# from dotenv import load_dotenv
from threading import Thread

class start():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    def __init__(self):
        pass
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

starte = serverSocket.ServerSocket()
starte.connect()