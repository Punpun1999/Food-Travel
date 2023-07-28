class Ubicacion:
    def __init__(self, id, direccion, coordenadas):
        self.id = id
        self.direccion = direccion
        self.coordenadas = coordenadas

    def to_dict(self):
        return self.__dict__