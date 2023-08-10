class Actividad:
    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destino_id": self.destino_id,
            "hora_inicio": self.hora_inicio
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["nombre"],
            data["destino_id"],
            data["hora_inicio"]
        )
