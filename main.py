import serverSocket
from threading import Thread


class start():
    def __init__(self):
        pass
    def acceptRequests(self):

    def sendAReply(self):

    def databaseSync(self):

    def checkSocket(self):
        lockCheckSocket = threading.Lock()
        lockCheckSocket.acquire()
        try:
            self.lcs = Thread(target=serverSocket.ServerSocket)
            self.lcs.start()
        finally:
            lockCheckSocket.release()

    def startSocket(self):

    def recordsLogs(self):
