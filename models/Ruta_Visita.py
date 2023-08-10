class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destinos": self.destinos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["nombre"],
            data["destinos"]
        )
