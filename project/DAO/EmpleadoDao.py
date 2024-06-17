from project.DAO.DataBaseConnectionDao import DataBaseConnectionDao


class EmpleadoDao(DataBaseConnectionDao):

    def get_workers(self):
        cursor = self.cursor
        query = 'CALL show_empleados();'
        cursor.execute(query)
        result = cursor.fetchall()
        self.close_cursor()
        return result

    def get_worker(self, id_empleado):
        cursor = self.cursor
        query = f'CALL show_empleado({id_empleado});'
        cursor.execute(query)
        result = cursor.fetchone()
        self.close_cursor()
        return result
