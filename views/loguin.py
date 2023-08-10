import os
import tkinter as tk
import json
from tkinter import messagebox
from views.registro_usuario import VentanaRegistro
from views.mapa_destinos import MapaDestinosCulinarios

class VentanaInicioSesion:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")

        self.nombre_usuario_var = tk.StringVar()
        self.contraseña_var = tk.StringVar()

        tk.Label(self.root, text="Nombre de Usuario:").pack()
        tk.Entry(self.root, textvariable=self.nombre_usuario_var).pack()

        tk.Label(self.root, text="Contraseña:").pack()
        tk.Entry(self.root, textvariable=self.contraseña_var, show="*").pack()

        tk.Button(self.root, text="Iniciar Sesión", command=self.iniciar_sesion).pack()
        tk.Button(self.root, text="Registrarse", command=self.abrir_ventana_registro).pack()

    def iniciar_sesion(self):
        nombre_usuario = self.nombre_usuario_var.get()
        contraseña = self.contraseña_var.get()

        # Obtener la ruta absoluta del archivo JSON
        carpeta_data = os.path.join(os.getcwd(), "data")
        ruta_archivo_json = os.path.join(carpeta_data, "usuarios.json")

        # Leer los usuarios del archivo JSON
        if os.path.exists(ruta_archivo_json):
            with open(ruta_archivo_json, "r") as archivo:
                usuarios = json.load(archivo)
        else:
            usuarios = []

        # Verificar las credenciales ingresadas con los datos almacenados en el archivo JSON
        for usuario in usuarios:
            if usuario["nombre_usuario"] == nombre_usuario and usuario["contraseña"] == contraseña:
                messagebox.showinfo("Inicio de Sesión", f"Inicio de sesión exitoso. Usuario: {nombre_usuario}")
                self.abrir_ventana_principal()
                return

        messagebox.showerror("Inicio de Sesión", "Credenciales incorrectas. Vuelve a intentarlo.")

    def abrir_ventana_registro(self):
        ventana_registro = tk.Toplevel(self.root)
        ventana_registro.title("Registro de Usuario")
        VentanaRegistro(ventana_registro)

