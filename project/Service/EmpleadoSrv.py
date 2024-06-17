from project.DAO.EmpleadoDao import EmpleadoDao
from project.DTO.EmpleadoDto import EmpleadoDto


class EmpleadoSrv:
    @staticmethod
    def find_workers():
        worker = EmpleadoDao()
        result = worker.get_workers()
        array = []
        for i in result:
            worker = EmpleadoDto(
                id_empleado=i[0],
                id_tipo_empleado=i[1],
                id_modalidad=i[2],
                id_rol=i[3],
                id_huella=i[4],
                id_token=i[5],
                num_identificacion=i[6],
                nombre_completo=i[7],
                correo=i[8],
                estado=i[9]
            )
            array.append(worker)
        return array

    @staticmethod
    def find_worker(id_empleado):
        worker = EmpleadoDao()
        result = worker.get_worker(id_empleado)
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
