import osmnx as ox
import pickle
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from geopy.geocoders import Nominatim
import time
from scenes import *
from Manager import *
# Suponiendo que style es un módulo con tus configuraciones de estilo
from constants import style

# Cargar el grafo desde el archivo
with open(style.file, "rb") as file:
    graph = pickle.load(file)

# crear figura y ejes para el grafo
fig, ax = ox.plot_graph(
    graph,        # el grafo a mostrar
    show=False,   # no mostrar ventana
    close=False,  # no cerrar el gráfico
    edge_color=style.edge_color,
    edge_alpha=0.3,
    node_size=0,
    bgcolor=style.verdelimaOscuro
)

# ventana principal
window = Manager()

# frame principal
app = createFrame(
    window,
    relh=1,
    relw=1,
)

# Frame del mapa
frame_1 = tk.Frame(app, background=style.verdelimaOscuro)
frame_1.place(
    relx=0,  # Frame en el lado izquierdo
    rely=0,
    relwidth=0.5,  # Ancho relativo
    relheight=0.5,
)

# funcion para obtener coordenadas de una dirección
def get_coordinates(address):
    geolocator = Nominatim(user_agent="elpapu")
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None

# funcion para actualizar el mapa en el canvas
def actualizarMapa(frame):
    canva = FigureCanvasTkAgg(fig, master=frame)
    canva.draw()
    canva.get_tk_widget().config(bg=style.verdelimaOscuro, cursor="cross")
    canva.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    return canva    

# canvas que contiene el mapa
canva = actualizarMapa(frame_1)

# Función para ejecutar cuando se presiona el botón "Encontrar"
def ejecutAlg():
    address = campo_texto.get()
    address += ", Villavicencio, Colombia"
    
    
    coordinates = get_coordinates(address)
    if coordinates:
        lat, lng = coordinates
        nearest_node = ox.distance.nearest_nodes(graph, lng, lat)
        node_x, node_y = graph.nodes[nearest_node]['x'], graph.nodes[nearest_node]['y']
        
        # Marcar el nodo en el gráfico
        ax.plot(node_x, node_y, 'ro', markersize=2)
        actualizarMapa(frame_1)  # Actualizar el canvas con el nuevo punto
    else:
        print("No se encontró la dirección")

# Frame del texto debajo del mapa
frame_2 = createFrame(
    app,
    xrel=0,
    yrel=0.5,
    relw=0.5,
    relh=0.1,
    cursor="xterm"
)

# Texto dentro del frame debajo del mapa
texto = tk.Text(
    master=frame_2,
    font=style.font,
    background=style.verdelimaOscuro,
    fg="white"
)
texto.pack(
    fill=tk.BOTH,
    expand=1
)
texto.insert(tk.END, "Hola, this is villavo")  
texto.config(state=tk.DISABLED)

# Frame del campo (input) de texto y botón
frame_3 = createFrame(
    app,
    xrel=0.5,
    relh=0.5,
    relw=0.3,
    bgcolor=style.backgroundColor
)

# Campo de entrada de texto
campo_texto = tk.Entry(frame_3)
campo_texto.place(
    relx=0.5,
    rely=0.05,
    relheight=0.075,
    width=400
)

# Botón de encontrar
btn = createButton(
    frame_3,
    accion=ejecutAlg,
    texto="Encontrar",
    xrel=0.65,
    yrel=0.125
)

# Frame inferior para posibles futuros usos
frame_4 = createFrame(
    app,
    xrel=0,
    yrel=0.95,
    relw=1,
    relh=0.08,
    bgcolor="white",
)

# Función para redimensionar el canvas
def resize_canvas(event):
    canva.get_tk_widget().config(width=event.width, height=event.height)
    canva.draw()

frame_1.bind('<Configure>', resize_canvas)

window.protocol("WM_DELETE_WINDOW", window.on_closing)
window.mainloop()
