import mariadb
import os, functools
from itertools import product
from sqlCommand import Command
from dotenv import load_dotenv


class Connections(): #connection DB, dataBasa = choice DB, commandData = sql command, soed = for inseert, update and delete command
    def __init__(self):
        pass

    def connect(self, dataBasa, commandData, soed=False):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        try:
            self.conn_params = {
                "user": os.environ.get('user'),
                "password": os.environ.get('password'),
                "host": os.environ.get('host1'),
                "database": os.environ.get(f'{dataBasa}')
            }
            zapros = (self.conn_params)
            self.connection = mariadb.connect(**zapros)
            cursor = self.connection.cursor()
            dateras = f"""SELECT * FROM reminder WHERE reminder.remind_at < DATE_ADD(DATE_SUB(NOW(), INTERVAL 3 HOUR), INTERVAL 1 MINUTE ) AND reminder.remind_at > DATE_ADD(DATE_SUB(NOW(), INTERVAL 3 HOUR), INTERVAL 1 SECOND ) AND reminder.user_name='admin';"""
            if soed == False:
                cursor.execute(dateras)
                row = cursor.fetchall()
                cursor.close()
                self.connection.close()
                # print(row)
                if not row:
                    return False
                return row
            if soed:
                cursor.execute(f"""{commandData}""", soed)
                self.connection.commit()
                cursor.close()
                self.connection.close()
                return True
        except:
            print('error connect')

class DataSync(Connections, Command): # sync ExpoCRM-DB and python-DB
    def __init__(self):
        self.requsetTask = str()
        super().CommandSQL()
        self.contactMySQL = 0
        self.spisokDlyaSravneniya = []
        self.spisokDlyaSravneniyaDva = []
        self.spisokDlyaSravneniyaTri = []
        # self.basa = self.requestEspoCRM('databaseOne', self.mySqlCommandProverka)
        # self.addData(self.basa, 'databaseTwo', self.mySqlCommandSozdanie)

    def sravnenie(self, database): # transfers the Espo-DB reminder to python-DB and delete the old python-DB reminder
        result1 = list(set(self.spisokDlyaSravneniya) - set(self.spisokDlyaSravneniyaDva))
        result2 = list(set(self.spisokDlyaSravneniyaDva) - set(self.spisokDlyaSravneniya))
        if result1:#transfer
            for i in result1:
                commandi = (f"INSERT INTO reminder(reminder_id, user_name, text_name, descriptions, remind_at, start_at) VALUES (?,?,?,?,?,?)")
                self.connect(database, commandi, i)
        if result2:#delete
            for i in result2:
                commandi = (f"DELETE FROM reminder WHERE reminder_id=?")
                turle = (i[0],)
                self.connect(database, commandi, turle)
        self.spisokDlyaSravneniya = 0
        self.spisokDlyaSravneniyaDva = 0
        self.spisokDlyaSravneniyaTri = 0
        self.contactMySQL = 0
        print(result1)
        print(result2)
        print(self.spisokDlyaSravneniya)
        print(self.spisokDlyaSravneniyaDva)
    def requestEspoCRM(self, database, commandMysql, soed=False): #connect EspoCRM and request all reminder
        try:
            row = self.connect(database, commandMysql, soed)
            return row
        except:
            print('error')
    def addData(self, database, commandMysql): #connect pythhon-DB and request all reminder
        try:
            self.spisokDlyaSravneniyaDva = self.connect(database, commandMysql, False)
            self.sravnenie(database)
        except:
            print('error')

    def startMysql(self):
        if not self.contactMySQL:
            self.contactMySQL = 1
            les = self.requestEspoCRM(database='databaseOne', commandMysql=self.requestReminder)
            for i in range(len(les)):
                self.raz = les[i][0]
                self.dva = les[i][1]
                self.tri = les[i][2]
                self.requsetTask = f"""SELECT reminder.id, user.user_name, {self.raz}.name, {self.raz}.description, reminder.remind_at, reminder.start_at
            from user
            join {self.raz} on {self.raz}.assigned_user_id = user.id
            join reminder on reminder.entity_id = {self.raz}.id
            WHERE reminder.deleted != 1 and reminder.entity_type = '{self.dva}' and reminder.entity_id = '{self.tri}' and reminder.type = 'Popup';"""
                let = self.requestEspoCRM(database='databaseOne', commandMysql=self.requsetTask)
                self.spisokDlyaSravneniya.append(tuple(let[0]))
            self.addData('databaseTwo', self.mySqlCommandSozdanie)

    def RequestDataBase(self):
        if not self.contactMySQL:
            self.contactMySQL = 1
            zapros = self.connect('databaseTwo', self.requestMySQL)
            if not zapros:
                print('da')
            # zapros = self.connect('databaseTwo', requestMySQL, self.transformLogin)
            self.contactMySQL = 0

sin = DataSync()
sin.RequestDataBase()
