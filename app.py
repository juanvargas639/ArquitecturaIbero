import tkinter as tk
from tkinter import messagebox, Scrollbar
from Main import MainLogica

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Buscar Ruta Óptima")

        # Configuración de colores y fuentes
        bg_color = "#f0f0f0"  # Color de fondo
        font_style = ("Arial", 12)  # Fuente

        # Frame principal
        frame = tk.Frame(root, padx=30, pady=30, bg=bg_color)
        frame.pack(fill="both", expand=True)

        # Listbox para mostrar las estaciones disponibles
        self.listbox = tk.Listbox(frame, font=font_style)
        self.listbox.pack(side="left", fill="both", expand=True)

        # Barra de desplazamiento
        scrollbar = Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        # Configuración de la barra de desplazamiento
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Asociar evento de clic al Listbox
        self.listbox.bind("<Double-Button-1>", self.mostrar_conexiones)

        self.mostrar_estaciones_disponibles()

        # Etiqueta y entrada para la estación de origen
        self.label_origen = tk.Label(root, text="Estación de origen:", font=font_style, bg=bg_color)
        self.label_origen.pack()
        self.entry_origen = tk.Entry(root, font=font_style)
        self.entry_origen.pack()

        # Etiqueta y entrada para la estación de destino
        self.label_destino = tk.Label(root, text="Estación de destino:", font=font_style, bg=bg_color)
        self.label_destino.pack()
        self.entry_destino = tk.Entry(root, font=font_style)
        self.entry_destino.pack()

        # Botón para iniciar la búsqueda de la ruta óptima
        self.button_buscar = tk.Button(root, text="Buscar Ruta", font=font_style, command=self.buscar_ruta)
        self.button_buscar.pack()

    def buscar_ruta(self):
        origen = self.entry_origen.get().capitalize()
        destino = self.entry_destino.get().capitalize()
        # Validar que se ingresaron estaciones de origen y destino
        if not origen or not destino:
            messagebox.showerror("Error", "Por favor ingrese la estación de origen y destino.")
            return
        # Encontrar estaciones cercanas
        estacion_origen = MainLogica.encontrar_estacion_cercana(origen)
        estacion_destino = MainLogica.encontrar_estacion_cercana(destino)
        if not estacion_origen or not estacion_destino:
            messagebox.showerror("Error", "No se encontró una estación cercana. Intente de nuevo.")
            return
        # Encontrar la ruta óptima
        ruta_optima, costo_total_pasaje = MainLogica.encontrar_ruta(estacion_origen, estacion_destino)
        if ruta_optima:
            ruta_str = ' -> '.join(ruta_optima)
            messagebox.showinfo("Ruta Óptima Encontrada", f"El mejor trayecto desde {estacion_origen} hasta {estacion_destino} es realizar las siguientes paradas: {ruta_str}. \nCosto total del pasaje: {costo_total_pasaje} pesos")
        else:
            messagebox.showinfo("Ruta no Encontrada", f"No se encontró ruta desde {estacion_origen} hasta {estacion_destino}")

    def mostrar_estaciones_disponibles(self):
        rutas = MainLogica.obtener_estaciones_disponibles()
        for ruta in rutas:
            self.listbox.insert("end", ruta)

    def mostrar_conexiones(self, event):
        index = self.listbox.curselection()
        if not index:
            return
        estacion_seleccionada = self.listbox.get(index)
        MainLogica.mostrar_conexiones(estacion_seleccionada, self.root)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
