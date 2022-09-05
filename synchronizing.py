import mariadb
import os
from dotenv import load_dotenv

class Connections(): #connection DB, dataBasa = base EspoCRM, commandData = sql command, soed = for inseert, update and delete command
    def connect(self, dataBasa, commandData, soed):
        try:
            dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
            if os.path.exists(dotenv_path):
                load_dotenv(dotenv_path)
            self.conn_params = {
                "user": os.environ.get('user'),
                "password": os.environ.get('password'),
                "host": os.environ.get('host'),
                "database": os.environ.get(f'{dataBasa}')
            }
            zapros = (self.conn_params)
            connection = mariadb.connect(**zapros)
            cursor = connection.cursor()
            if soed == False:
                cursor.execute(f"""{commandData}""")
                row = cursor.fetchall()
                cursor.close()
                connection.close()
                return row
            if soed:
                cursor.execute(f"""{commandData}""", soed)
                connection.commit()
                cursor.close()
                connection.close()
                return True
        except:
            print('error connect')

class Data(Connections): # sync ExpoCRM-DB and python-DB
    def sravnenie(self, row, basa, database): #
        result1 = list(set(basa) - set(row))
        result2 = list(set(row) - set(basa))
        if result1:
            for i in result1:
                commandi = (f"INSERT INTO notifications(notification_id, data, class, user) VALUES (?,?,?,?)")
                self.connect(database, commandi, i)
        if result2:
            for i in result2:
                commandi = (f"DELETE FROM notifications WHERE notification_id=?")
                turle = (i[0],)
                self.connect(database, commandi, turle)
    def requestEspoCRM(self, database, commandMysql, soed):
        try:
            row = self.connect(database, commandMysql, soed)
            return row
        except:
            print('error')
    def addData(self, basa, database, commandMysql, soed): #connect pythhon-DB and request all reminder
        try:
            row = self.connect(database, commandMysql, soed)
            self.sravnenie(row, basa, database)
        except:
            print('error')

mySqlCommandProverka = """
            SELECT reminder.id, reminder.remind_at, reminder.entity_type, user.user_name
            FROM reminder
            JOIN user ON reminder.user_id = user.id
            WHERE reminder.deleted != 1"""

mySqlCommandSozdanie = """
            SELECT notification_id, data, class, user
            FROM notifications"""

zapros = Data()
basa = zapros.requestEspoCRM('databaseOne', mySqlCommandProverka, False)
zapros.addData(basa, 'databaseTwo', mySqlCommandSozdanie, False)