import osmnx as ox
import tkinter as tk
import pickle
from constants import style
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from PIL import Image, ImageTk

class ZoomableCanvas(tk.Canvas):
    def __init__(self, master, img, **kwargs):
        super().__init__(master, **kwargs)
        self.img = img
        self.img_id = self.create_image(0, 0, anchor=tk.NW, image=self.img)
        self.scale_factor = 1.0
        self.bind("<MouseWheel>", self.zoom)
        self.bind("<Button-1>", self.start_pan)
        self.bind("<B1-Motion>", self.pan)

    def zoom(self, event):
        scale = 1.0
        if event.delta > 0:  # Zoom in
            scale *= 1.1
        elif event.delta < 0:  # Zoom out
            scale /= 1.1
        
        self.scale_factor *= scale
        self.scale("all", event.x, event.y, scale, scale)
        self.configure(scrollregion=self.bbox("all"))

    def start_pan(self, event):
        self.scan_mark(event.x, event.y)

    def pan(self, event):
        self.scan_dragto(event.x, event.y, gain=1)

def create_map():
    # Descargar y crear el grafo del mapa
    G = ox.graph_from_place("Piedmont, California, USA", network_type='drive')
    
    # Renderizar el grafo a una figura de Matplotlib
    fig, ax = ox.plot_graph(G, show=False, close=False)
    
    # Convertir la figura a una imagen
    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    img = Image.frombytes('RGB', canvas.get_width_height(), canvas.tostring_rgb())
    return ImageTk.PhotoImage(img)

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Zoom en Canvas de OSMnx")

    # Crear el mapa y obtener la imagen
    tk_img = create_map()

    # Crear el canvas y añadirlo a la ventana
    canvas = ZoomableCanvas(root, img=tk_img, width=800, height=600, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    # Ajustar el canvas para visualizar el grafo completo
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Ejecutar el bucle principal de la aplicación
    root.mainloop()

main()
