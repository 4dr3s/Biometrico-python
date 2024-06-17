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
        return worker

    @staticmethod
    def find_workers():
        worker = EmpleadoDao()
        result = worker.get_workers()
        array = []
        for i in result:
            worker = EmpleadoSrv.json_format(i)
            array.append(worker)
        return array

    @staticmethod
    def find_worker(id_empleado):
        worker = EmpleadoDao()
        result = worker.get_worker(id_empleado)
        worker = EmpleadoSrv.json_format(result)
        return worker
