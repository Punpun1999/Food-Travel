import tkinter as tk
import json
import os
from models.Usuario import Usuario

class VentanaRegistro:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuario")

        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.correo_var = tk.StringVar()
        self.contraseña_var = tk.StringVar()
        self.nombre_usuario_var = tk.StringVar()

        # Crear campos de entrada
        tk.Label(self.root, text="Nombre:").pack()
        tk.Entry(self.root, textvariable=self.nombre_var).pack()

        tk.Label(self.root, text="Apellido:").pack()
        tk.Entry(self.root, textvariable=self.apellido_var).pack()

        tk.Label(self.root, text="Correo:").pack()
        tk.Entry(self.root, textvariable=self.correo_var).pack()

        tk.Label(self.root, text="Contraseña:").pack()
        tk.Entry(self.root, textvariable=self.contraseña_var).pack()

        tk.Label(self.root, text="Nombre de Usuario:").pack()
        tk.Entry(self.root, textvariable=self.nombre_usuario_var).pack()

        # Botón para guardar los datos en el archivo JSON
        tk.Button(self.root, text="Registrar", command=self.registrar_usuario).pack()

    def registrar_usuario(self):
        # Obtener los valores ingresados por el usuario
        nombre = self.nombre_var.get()
        apellido = self.apellido_var.get()
        correo = self.correo_var.get()
        contraseña = self.contraseña_var.get()
        nombre_usuario = self.nombre_usuario_var.get()

        # Crear una instancia del modelo Usuario con los datos ingresados
        nuevo_usuario = Usuario(nombre, apellido, correo, contraseña, nombre_usuario)

        # Guardar el usuario en el archivo JSON
        self.guardar_usuario_en_json(nuevo_usuario.to_dict())
 
    def guardar_usuario_en_json(self, usuario_dict):
        # Obtener la ruta absoluta de la carpeta "data"
        carpeta_data = os.path.join(os.getcwd(), "data")
        ruta_archivo_json = os.path.join(carpeta_data, "usuarios.json")
        # Crear la carpeta "data" si no existe
        if not os.path.exists(carpeta_data):
            os.makedirs(carpeta_data)

        # Combinar la ruta de la carpeta con el nombre del archivo JSON
        ruta_archivo_json = os.path.join(carpeta_data, "usuarios.json")

        # Lógica para guardar el usuario en el archivo JSON
        # Verificar si el archivo ya existe
        if os.path.exists(ruta_archivo_json):
            # Leer los usuarios actuales del archivo
            with open(ruta_archivo_json, "r") as archivo:
                usuarios = json.load(archivo)
        else:
            # Si el archivo no existe, crear una lista vacía de usuarios
            usuarios = []

        # Agregar el nuevo usuario a la lista
        usuarios.append(usuario_dict)

        # Guardar la lista actualizada de usuarios en el archivo JSON
        with open(ruta_archivo_json, "w") as archivo:
            json.dump(usuarios, archivo)


if __name__ == "__main__":
    root = tk.Tk()
    ventana = VentanaRegistro(root)
    root.mainloop()