import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import json
from tkintermapview import TkinterMapView
from models.destino_culunario import DestinoCulinario


class MapaDestinosCulinarios:
    def __init__(self, root, destinos_json_path):
        self.root = root
        self.root.title("Mapa de Destinos Culinarios en Salta")

        self.destinos_json_path = destinos_json_path
        self.destinos_culinarios = self.cargar_destinos_culinarios()
        self.frame_mapa = tk.Frame(self.root, width=600, height=600)
        self.frame_mapa.pack(side='right')

        # Crear el mapa en blanco
        self.mapa = TkinterMapView(self.frame_mapa, width=600, height=600)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(side='right')

        self.mostrar_marcadores_guardados()
        self.marcadores = []

        # Agregar el botón "Agregar Destino"
        tk.Button(self.root, text="Agregar Destino", command=self.mostrar_ventana_agregar_destino).pack()
        # Agregar el boton "Mostrar lista de Destinos"
        tk.Button(self.root, text="Mostrar Lista de Destinos", command=self.mostrar_lista_destinos).pack()



    def cargar_destinos_culinarios(self):
        destinos_culinarios = []
        if os.path.exists(self.destinos_json_path):
            print("Cargando datos desde el archivo JSON...")
            with open(self.destinos_json_path, "r") as archivo:
                data = json.load(archivo)
            for destino_data in data:
                destino = DestinoCulinario(**destino_data)
                destinos_culinarios.append(destino)
            print("Datos cargados:", destinos_culinarios)
        return destinos_culinarios
    
    def mostrar_marcadores_guardados(self):
        for destino in self.destinos_culinarios:
            marker = self.mapa.set_marker(destino.latitud, destino.longitud, text=destino.nombre)

            # Establecer el texto del marcador
            texto_marcador = f"{destino.nombre}\n{destino.tipo_cocina}\nPrecio: {destino.precio_minimo}-{destino.precio_maximo}"
            marker.set_text(texto_marcador)

    def guardar_destinos_culinarios(self):
        data = [destino.to_dict() for destino in self.destinos_culinarios]
        with open(self.destinos_json_path, "w") as archivo:
            json.dump(data, archivo)

    def agregar_marcador_mapa(self, destino):
        marker = self.mapa.set_marker(destino.latitud, destino.longitud, text=destino.nombre)
        self.marcadores.append(marker)
        
    def refrescar_mapa(self):
        self.mapa.update()

    def mostrar_lista_destinos(self):
        ventana_lista = tk.Toplevel(self.root)
        ventana_lista.title("Lista de Destinos Culinarios")

        lista_destinos = tk.Listbox(ventana_lista, width=50, height=20)
        lista_destinos.pack()

        for destino in self.destinos_culinarios:
            lista_destinos.insert(tk.END, destino.nombre)

    def mostrar_ventana_agregar_destino(self):
        ventana_agregar_destino = tk.Toplevel(self.root)
        ventana_agregar_destino.title("Agregar Destino Culinario")

        tk.Label(ventana_agregar_destino, text="ID:").pack()
        id_var = tk.IntVar()
        tk.Entry(ventana_agregar_destino, textvariable=id_var).pack()

        tk.Label(ventana_agregar_destino, text="Nombre:").pack()
        nombre_var = tk.StringVar()
        tk.Entry(ventana_agregar_destino, textvariable=nombre_var).pack()

        tk.Label(ventana_agregar_destino, text="Tipo de Cocina:").pack()
        tipo_cocina_var = tk.StringVar()
        tk.Entry(ventana_agregar_destino, textvariable=tipo_cocina_var).pack()

        tk.Label(ventana_agregar_destino, text="Ingredientes (separados por comas):").pack()
        ingredientes_var = tk.StringVar()
        tk.Entry(ventana_agregar_destino, textvariable=ingredientes_var).pack()

        tk.Label(ventana_agregar_destino, text="Precio Mínimo:").pack()
        precio_minimo_var = tk.DoubleVar()
        tk.Entry(ventana_agregar_destino, textvariable=precio_minimo_var).pack()

        tk.Label(ventana_agregar_destino, text="Precio Máximo:").pack()
        precio_maximo_var = tk.DoubleVar()
        tk.Entry(ventana_agregar_destino, textvariable=precio_maximo_var).pack()

        tk.Label(ventana_agregar_destino, text="Popularidad:").pack()
        popularidad_var = tk.DoubleVar()
        tk.Entry(ventana_agregar_destino, textvariable=popularidad_var).pack()

        tk.Label(ventana_agregar_destino, text="Disponibilidad (1: Disponible, 0: No Disponible):").pack()
        disponibilidad_var = tk.IntVar()
        tk.Entry(ventana_agregar_destino, textvariable=disponibilidad_var).pack()

        tk.Label(ventana_agregar_destino, text="ID Ubicación:").pack()
        id_ubicacion_var = tk.IntVar()
        tk.Entry(ventana_agregar_destino, textvariable=id_ubicacion_var).pack()

        tk.Label(ventana_agregar_destino, text="URL de la imagen:").pack()
        imagen_var = tk.StringVar()
        tk.Entry(ventana_agregar_destino, textvariable=imagen_var).pack()

        tk.Label(ventana_agregar_destino, text="Latitud:").pack()
        latitud_var = tk.DoubleVar()
        tk.Entry(ventana_agregar_destino, textvariable=latitud_var).pack()

        tk.Label(ventana_agregar_destino, text="Longitud:").pack()
        longitud_var = tk.DoubleVar()
        tk.Entry(ventana_agregar_destino, textvariable=longitud_var).pack()

        tk.Button(ventana_agregar_destino, text="Guardar", command=lambda: self.guardar_destino_culinario(
            ventana_agregar_destino,
            id_var.get(),
            nombre_var.get(),
            tipo_cocina_var.get(),
            ingredientes_var.get().split(','),
            precio_minimo_var.get(),
            precio_maximo_var.get(),
            popularidad_var.get(),
            disponibilidad_var.get(),
            id_ubicacion_var.get(),
            imagen_var.get(),
            latitud_var.get(),
            longitud_var.get()
        )).pack()

    def guardar_destino_culinario(self, ventana_agregar_destino, id, nombre, tipo_cocina, ingredientes, precio_minimo,
                                  precio_maximo, popularidad, disponibilidad, id_ubicacion, imagen, latitud, longitud):
        nuevo_destino = DestinoCulinario(
            id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad,
            id_ubicacion, imagen, latitud, longitud
        )
        self.destinos_culinarios.append(nuevo_destino)
        self.agregar_marcador_mapa(nuevo_destino) 
        self.guardar_destinos_culinarios()
        self.refrescar_mapa()
        ventana_agregar_destino.destroy()