import json

class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen, latitud, longitud):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen
        self.latitud = latitud
        self.longitud = longitud
        
    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)

