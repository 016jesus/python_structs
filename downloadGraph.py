import osmnx as ox
import pickle

# Descargar el grafo de una ubicación específica

ubicacion = ""
grafo = ox.graph_from_place(ubicacion, network_type='drive')

# Guardar el grafo localmente utilizando pickle
name = f"grafo_{ubicacion}_osmnx.pkl"    
# wb para escribir en el archivo
with open(name, "wb") as file:
    pickle.dump(grafo, file)
    print(f"Grafo descargado y guardado en {name}")
