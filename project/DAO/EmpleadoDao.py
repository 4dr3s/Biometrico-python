from project.Connection.db import db


class EmpleadoDao:

    def __init__(self):
        self.connection = db.get_db()
        self.cursor = self.connection.cursor()

    def get_workers(self):
        cursor = self.cursor
        query = 'CALL show_empleados()'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
