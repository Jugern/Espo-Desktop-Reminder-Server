
mySqlCommandProverka = """
            SELECT reminder.id, reminder.remind_at, reminder.entity_type, user.user_name
            FROM reminder
            JOIN user ON reminder.user_id = user.id
            WHERE reminder.deleted != 1"""

mySqlCommandSozdanie = """
            SELECT notification_id, data, class, user
            FROM notifications"""

mySqlCommandVseApi = """
            SELECT user.id, user.name, user.deleted, user.user_name, user.api_key, is_active
            FROM user
            WHERE user.type = 'api'"""