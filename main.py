import tkinter as tk
from views.mapa_destinos import MapaDestinosCulinarios
from views.loguin import VentanaInicioSesion

if __name__ == "__main__":
    root = tk.Tk()

    # Ruta del archivo JSON con los datos de los destinos culinarios
    destinos_json_path = "data/destinos_culinarios.json"
    mapa_destinos = MapaDestinosCulinarios(root, destinos_json_path)
    ventana_inicio=VentanaInicioSesion(root)
    root.mainloop()
