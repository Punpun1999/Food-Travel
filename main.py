import tkinter as tk

class FoodTravelApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Food Travel")
        self.geometry("800x600")
        # Título de la aplicación
        title_label = tk.Label(self, text="Bienvenido a Food Travel", font=("Helvetica", 20))
        title_label.pack(pady=20)
if __name__ == "__main__":
    app = FoodTravelApp()
    app.mainloop()
