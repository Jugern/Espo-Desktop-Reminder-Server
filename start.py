import mariadb
import os
from dotenv import load_dotenv

class Connections():
    def connect(self, dataBasa, commandData):
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
            cursor.execute(f"""{commandData}""")
            row = cursor.fetchall()
            cursor.close()
            connection.close()
            return row
        except:
            print('error')

class Data(Connections):
    def sravnenie(self, row, basa):
        result1 = list(set(basa) - set(row))
        result2 = list(set(row) - set(basa))
        print(result1)
        print(result2)

    def addData(self, basa, database, commandMysql):
        try:
            row = self.connect(database, commandMysql)
            self.sravnenie(row, basa)
        except:
            print('error')

mySqlCommandProverka = """
            SELECT reminder.id, reminder.remind_at, reminder.entity_type, user.user_name
            FROM reminder
            JOIN user ON reminder.user_id = user.id
            WHERE reminder.deleted != 1"""

mySqlCommandSozdanie = """
            SELECT id, data, class, user
            FROM notifications"""

zapros = Connections()
basa = zapros.connect('database', mySqlCommandProverka)
zapros = Data()
zapros.addData(basa, 'databaseTwo', mySqlCommandSozdanie)