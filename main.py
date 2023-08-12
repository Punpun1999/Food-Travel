import tkinter as tk
from views.loguin import VentanaInicioSesion

if __name__ == "__main__":
    root = tk.Tk()

    # Ruta del archivo JSON con los datos de los destinos culinarios
    destinos_json_path = "data/destinos_culinarios.json"
    
    # Crea una instancia de la ventana de inicio de sesión
    ventana_inicio = VentanaInicioSesion(root)
    
    # Inicia el bucle principal de la aplicación
    root.mainloop()