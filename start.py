import mariadb
import os
from dotenv import load_dotenv

class Connections():
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
            # print(commandData)
            # print(soed)
            if soed == False:
                cursor.execute(f"""{commandData}""")
                row = cursor.fetchall()
                cursor.close()
                connection.close()
                # print(row)
                return row
            if soed:
                cursor.execute(f"""{commandData}""", soed)
                connection.commit()
                cursor.close()
                connection.close()
                # print(soed)
                return True
        except:
            print('error')

class Data(Connections):
    def sravnenie(self, row, basa, database):
        result1 = list(set(basa) - set(row))
        result2 = list(set(row) - set(basa))
        for i in result1:
            commandi = (f"INSERT INTO notifications(notification_id, data, class, user) VALUES (?,?,?,?)")
            self.connect(database, commandi, i)
        for i in result2:
            commandi = (f"DELETE FROM notifications WHERE notification_id=?")
            turle = (i[0],)
            self.connect(database, commandi, turle)
        print(result1)
        print(result2)

    def addData(self, basa, database, commandMysql, soed):
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

zapros = Connections()
basa = zapros.connect('database', mySqlCommandProverka, False)
zapros = Data()
zapros.addData(basa, 'databaseTwo', mySqlCommandSozdanie, False)