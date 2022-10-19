
class Command():
    def __init__(self):
        pass
    def CommandSQL(self):
        self.mySqlCommandProverka = """
            SELECT reminder.id, reminder.remind_at, reminder.entity_type, user.user_name
            FROM reminder
            JOIN user ON reminder.user_id = user.id
            WHERE reminder.deleted != 1"""

        self.mySqlCommandSozdanie = """
            SELECT notification_id, data, class, user
            FROM notifications"""

        self.mySqlCommandVseApi = """
            SELECT user.id, user.name, user.deleted, user.user_name, user.api_key, is_active
            FROM user
            WHERE user.type = 'api'"""

        self.mySqlCommandAcceptRequest = """
            SELECT notification_id, data, class, user
            FROM notifications
            WHERE user=?"""