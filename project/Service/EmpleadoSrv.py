from project.DAO.EmpleadoDao import EmpleadoDao
from project.DTO.EmpleadoDto import EmpleadoDto


class EmpleadoSrv:
    @staticmethod
    def json_format(result):
        worker = EmpleadoDto(
            id_empleado=result[0],
            id_tipo_empleado=result[1],
            id_modalidad=result[2],
            id_rol=result[3],
            id_huella=result[4],
            id_token=result[5],
            num_identificacion=result[6],
            nombre_completo=result[7],
            correo=result[8],
            estado=result[9]
        )
        return worker.to_json()

    @staticmethod
    def find_workers(session):
        connection = EmpleadoDao(session)
        result = connection.get_workers()
        array = [EmpleadoSrv.json_format(i) for i in result]
        return array

    @staticmethod
    def find_worker(session, id_empleado):
        connection = EmpleadoDao(session)
        result = connection.get_worker(id_empleado)
        worker = EmpleadoSrv.json_format(result)
        return worker
