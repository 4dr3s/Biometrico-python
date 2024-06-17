from project.Connection.db import db


class HorarioDao:

    def __init__(self):
        self.connect = db.get_db()
        self.cursor = self.connect.cursor()

