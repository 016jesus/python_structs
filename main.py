from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from geopy.geocoders import Nominatim
from scenes import *
from Manager import *
from constants import style

# cargar el grafo desde el archivo
with open(style.file, "rb") as file:
    graph = pickle.load(file)

# crear figura y ejes para el grafo
fig, ax = ox.plot_graph(
    graph,        # el grafo a mostrar
    show=False,   # no mostrar ventana
    close=False,  # no cerrar el grafico
    edge_color=style.edge_color,
    edge_alpha=0.3,
    node_size=0,
    dpi = 0,
    bgcolor=style.backgroundColor
)

# ventana principal
window = Manager()
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

# frame principal
app = createFrame(
    window,
    relh=1,
    relw=1,
)

# Frame del mapa
frame_1 = tk.Frame(app, background=style.backgroundColor)
frame_1.place(
    relx=0,  # Frame en el lado izquierdo
    rely=0.1,
    relwidth=0.7,  # Ancho relativo
    relheight=0.9
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
    canva.get_tk_widget().config(bg=style.backgroundColor, cursor="cross")
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
        print("No se encontro la direccion")

# Frame del texto debajo del mapa
frame_2 = createFrame(
    app,
    xrel=0,
    yrel=0,
    relw=1,
    relh=0.1,
    cursor="xterm"
)

# Texto dentro del frame debajo del mapa
texto = tk.Text(
    master=frame_2,
    font=style.font,
    
    background=style.main,
    fg="black"
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
    xrel=0.7,
    yrel=0.1,
    relh=0.9,
    relw=0.3,
    bgcolor=style.backgroundColor
)

# Campo de entrada de texto
campo_texto = tk.Entry(frame_3, relief="groove")
campo_texto.place(
    relx=0.4,
    rely=0.05,
    relheight=0.05,
    width=400
)

# Botón de encontrar
btn = createButton(
    frame_3,
    accion=ejecutAlg,
    texto="Encontrar",
    xrel=0.65,
    yrel=0.1
)

# Frame inferior para posibles futuros usos
frame_4 = createFrame(
    app,
    xrel=0,
    yrel=0.95,
    relw=1,
    relh=0.05,
    bgcolor="white",
)

# Funcion para redimensionar el canvas
def resize_canvas(event):
    canva.get_tk_widget().config(width=event.width, height=event.height)
    canva.draw()

def on_zoom(event):

    
    canva.draw_idle()  # Actualizar el canvas

# Conectar el evento de zoom al manejador de eventos



frame_1.bind('<Configure>', resize_canvas)

window.protocol("WM_DELETE_WINDOW", window.on_closing)
window.mainloop()
