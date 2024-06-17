class HorarioDto:
    def __init__(self, id_horario, id_empleado, id_dia, hora_inicio, hora_final):
        self.id_horario = id_horario,
        self.id_empleado = id_empleado,
        self.id_dia = id_dia,
        self.hora_inicio = hora_inicio,
        self.hora_final = hora_final

    def to_json(self):
        return {
            'id_horario': self.id_horario,
            'id_empleado': self.id_empleado,
            'id_dia': self.id_dia,
            'hora_inicio': self.hora_inicio,
            'hora_final': self.hora_final
        }
