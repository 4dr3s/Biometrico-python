from project.Connection.db import db


class DataBaseConnectionDao:
    def __init__(self):
        self.connection = db.get_db()
        self.cursor = self.connection.cursor()

    def close_cursor(self):
        self.cursor.close()
