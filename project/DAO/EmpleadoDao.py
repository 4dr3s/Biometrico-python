from sqlalchemy import text


class EmpleadoDao:

    def __init__(self, session):
        self.session = session

    def get_workers(self):
        result = self.session.execute(text('Call show_empleados();'))
        return result.fetchall()

    def get_worker(self, id_empleado):
        result = self.session.execute(text('Call show_empleado(:id);'), {'id': id_empleado})
        return result.fetchone()
