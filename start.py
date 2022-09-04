import mariadb
import os
from dotenv import load_dotenv


class Notification():
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.conn_params = {
            "user": os.environ.get('user'),
            "password": os.environ.get('password'),
            "host": os.environ.get('host'),
            "database": os.environ.get('database')
        }
    def connect(self):
        zapros = (self.conn_params)
        connection = mariadb.connect(**zapros)
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT reminder.id, reminder.remind_at, reminder.entity_type, user.user_name
        FROM reminder
        JOIN user ON reminder.user_id = user.id
        WHERE reminder.deleted != 1""")
        row = cursor.fetchall()
        # print(row)
        # c = (row)
        # print(*c, ' ')
        cursor.close()
        connection.close()
        return row

class Data():
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)
        self.conn_params = {
            "user": os.environ.get('user'),
            "password": os.environ.get('password'),
            "host": os.environ.get('host'),
            "database": os.environ.get('databaseTwo')
        }

    def sravnenie(self, basa):
        result1 = list(set(basa) - set(self.row))
        result2 = list(set(self.row) - set(basa))
        print(result1)
        print(result2)

    def addData(self, basa):
        zapros = (self.conn_params)
        connection = mariadb.connect(**zapros)
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT id, data, class, user
        FROM notifications""")
        self.row = cursor.fetchall()
        cursor.close()
        connection.close()
        self.sravnenie(basa)




zapros = Notification()
basa = zapros.connect()
zapros = Data()
zapros.addData(basa)





