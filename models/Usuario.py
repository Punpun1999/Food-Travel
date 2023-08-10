class Usuario:
    last_id = 0  # Variable de clase para almacenar el último ID utilizado

    def __init__(self, nombre, apellido, correo, contraseña, nombre_usuario, historial_rutas=None):
        Usuario.last_id += 1  # Incrementar el ID al crear una nueva instancia
        self.id = Usuario.last_id  # Asignar el nuevo ID a la instancia actual
        self.nombre = nombre
        self.apellido = apellido
        self.historial_rutas = historial_rutas if historial_rutas is not None else []
        self.correo = correo
        self.contraseña = contraseña
        self.nombre_usuario = nombre_usuario

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "historial_rutas": self.historial_rutas,
            "nombre_usuario": self.nombre_usuario,
            "correo": self.correo,
            "contraseña": self.contraseña
        }
