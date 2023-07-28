class Review:
    def __init__(self, id, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_dict(self):
        return self.__dict__
