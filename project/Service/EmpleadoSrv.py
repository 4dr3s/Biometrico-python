from project.DAO.EmpleadoDao import EmpleadoDao
from project.DTO.EmpleadoDto import EmpleadoDto

# Esta es la clase de Empleado para los servicios


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
