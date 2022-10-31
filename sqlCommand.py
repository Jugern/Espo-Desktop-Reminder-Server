
class Command():
    def __init__(self):
        pass
    def CommandSQL(self):
        self.raz = str()
        self.dva = str()
        self.tri = str()
        self.requestReminder = """SELECT LOWER(reminder.entity_type), reminder.entity_type, reminder.entity_id FROM reminder"""

        self.requsetTask = f"""SELECT reminder.id, user.user_name, {self.raz}.name, {self.raz}.description, reminder.remind_at, reminder.start_at
from user
join {self.raz} on {self.raz}.assigned_user_id = user.id
join reminder on reminder.entity_id = {self.raz}.id
WHERE reminder.deleted != 1 and reminder.entity_type = '{self.dva}' and reminder.entity_id = '{self.tri}' and reminder.type = 'Popup';"""

        self.mySqlCommandProverka = """
            SELECT reminder.id, reminder.remind_at, reminder.entity_type, user.user_name
            FROM reminder
            JOIN user ON reminder.user_id = user.id
            WHERE reminder.deleted != 1"""

        self.mySqlCommandSozdanie = """
            SELECT reminder_id, user_name, text_name, descriptions, remind_at, start_at
            FROM reminder"""

        self.mySqlCommandVseApi = """
            SELECT user.id, user.name, user.deleted, user.user_name, user.api_key, is_active
            FROM user
            WHERE user.type = 'api'"""

        self.mySqlCommandAcceptRequest = """
            SELECT notification_id, data, class, user
            FROM notifications
            WHERE user=?"""

        self.mySqlEnterTable = """SELECT LOWER(reminder.entity_type) FROM reminder"""

        self.requestMySQL = f"""SELECT * FROM reminder WHERE reminder.remind_at < DATE_ADD(DATE_SUB(NOW(), INTERVAL 3 HOUR), INTERVAL 1 MINUTE ) AND reminder.remind_at > DATE_ADD(DATE_SUB(NOW(), INTERVAL 3 HOUR), INTERVAL 1 SECOND ) AND reminder.user_name=?;"""