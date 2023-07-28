class Usuario:
    def __init__(self, id, nombre, apellido, historial_rutas):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas

    def to_dict(self):
        return self.__dict__