class Ubicacion:
    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_dict(self):
        return {
            "id": self.id,
            "direccion": self.direccion,
            "coordenadas": self.coordenadas
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["direccion"],
            data["coordenadas"]
        )
