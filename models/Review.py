class Review:
    def __init__(self, id_destino, id_usuario, calificacion, comentario, animo):
        self.id = 0  # El identificador se generará al guardar la review en el archivo JSON
        self.id_destino = id_destino
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def to_dict(self):
        return {
            "id": self.id,
            "id_destino": self.id_destino,
            "id_usuario": self.id_usuario,
            "calificacion": self.calificacion,
            "comentario": self.comentario,
            "animo": self.animo
        }

    @classmethod
    def from_dict(cls, data):
        review = cls(
            data["id_destino"],
            data["id_usuario"],
            data["calificacion"],
            data["comentario"],
            data["animo"]
        )
        review.id = data["id"]  # Asignar el ID almacenado en el archivo JSON
        return review
