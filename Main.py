from Bibliotecas import *
# Aquí sigue el resto de tu código...
from Dataset import Dataset

class MainLogica:
    @staticmethod
    def mostrar_conexiones(estacion_seleccionada, root):  # Agrega 'root' como parámetro
            dataset_objeto = Dataset()
            dataset = dataset_objeto.obtener_dataset()
            conexiones = dataset.get(estacion_seleccionada.strip('- '))
            if conexiones:
                modal = Toplevel(root)  # Utiliza 'Toplevel' en lugar de 'tk.Toplevel'
                modal.title(f"Conexiones de {estacion_seleccionada}")
                conexiones_texto = "\n".join([f"- Estación {destino} con un costo de {costo}" for destino, costo in conexiones.items()])
                label = tk.Label(modal, text=conexiones_texto)
                label.pack()
            else:
                messagebox.showinfo("Conexiones no encontradas", f"No se encontraron conexiones para {estacion_seleccionada}")

    # Función para encontrar la mejor ruta desde un origen a un destino
    # Función para encontrar la mejor ruta desde un origen a un destino
    @staticmethod
    def encontrar_ruta(origen, destino):
        cola_prioridad = [(0, origen, [])]  
        visitados = set()
        # Crear el dataset utilizando la clase Dataset
        dataset_objeto = Dataset()
        dataset = dataset_objeto.obtener_dataset()
        while cola_prioridad:
            costo_acumulado, nodo_actual, ruta_hasta_nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == destino:
                costo_total_pasaje = costo_acumulado * 100  # Multiplicamos por 100 para obtener el costo en pesos
                return ruta_hasta_nodo_actual + [nodo_actual], costo_total_pasaje

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                if nodo_actual in dataset:  
                    for vecino, costo in dataset[nodo_actual].items():
                        nueva_ruta = ruta_hasta_nodo_actual + [nodo_actual]
                        heapq.heappush(cola_prioridad, (costo_acumulado + costo, vecino, nueva_ruta))

        return None, None

    
    # Función para encontrar la estación más cercana dado un nombre
    @staticmethod
    def encontrar_estacion_cercana(nombre_estacion):
        # Crear el dataset utilizando la clase Dataset
        dataset_objeto = Dataset()
        dataset = dataset_objeto.obtener_dataset()

        # Obtener la lista de estaciones a partir del dataset
        estaciones = list(dataset.keys())
        coincidencias = get_close_matches(nombre_estacion, estaciones, n=1, cutoff=0.6)
        if coincidencias:
            return coincidencias[0]
        else:
            return None

    @staticmethod 
    def obtener_estaciones_disponibles():
        estaciones = []
        estaciones.append("Estaciones disponibles en el sistema:")
        for estacion in Dataset.obtener_dataset().keys():
            estaciones.append(f"- {estacion}")
        return estaciones
    
    @staticmethod 
    def obtener_rutas_disponibles():
        rutas = []
        rutas.append("Rutas disponibles en el sistema:")
        for origen, destinos in Dataset.obtener_dataset().items():
            ruta = f"Desde la estación {origen} se puede llegar a:"
            for destino, costo in destinos.items():
                ruta += f"\n- Estación {destino} con un costo de {costo}"
            rutas.append(ruta)
        return rutas


if __name__ == "__main__":
    rutas = MainLogica.obtener_rutas_disponibles()
    for ruta in rutas:
        print(ruta)

