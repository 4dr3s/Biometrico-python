class EmpleadoDto:
    def __init__(self, id_empleado, id_tipo_empleado, id_modalidad, id_rol, id_huella, id_token, num_identificacion,
                 nombre_completo, correo, estado):
        self.id_empleado = id_empleado,
        self.id_tipo_empleado = id_tipo_empleado,
        self.id_modalidad = id_modalidad,
        self.id_rol = id_rol,
        self.id_huella = id_huella,
        self.id_token = id_token,
        self.num_identificacion = num_identificacion,
        self.nombre_completo = nombre_completo,
        self.correo = correo,
        self.estado = estado

    def to_json(self):
        return {
            'id_empleado': self.id_empleado,
            'id_tipo_empleado': self.id_tipo_empleado,
            'id_modalidad': self.id_modalidad,
            'id_rol': self.id_rol,
            'id_huella': self.id_huella,
            'id_token': self.id_token,
            'num_identificacion': self.num_identificacion,
            'nombre_completo': self.nombre_completo,
            'correo': self.correo,
            'estado': self.estado
        }
