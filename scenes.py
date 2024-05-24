import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import osmnx as ox
import matplotlib.pyplot as plt
from constants import style
import pickle
import pandas as pd
from geopandas import *
from geopy.geocoders import Nominatim

def createButton(
    parent,
    xrel = 0,
    yrel = 0,
    texto ="boton",
    accion = lambda: print("Hola"),
    font = style.font,
    fondo = style.negroBotones,
    ctext ='#FFFFFF',
    padx = 20,
    pady = 10,
    highlightcolor="#DFF2CD",
    highlightbackground="#10150C",
    justify = "left",
    relief = "ridge"):
    
        btn = tk.Button(
            parent,
            justify=justify,
            text=texto,
            command=accion,
            font=font,
            highlightbackground=highlightbackground,
            highlightcolor=highlightcolor,
            bg=fondo,
            fg=ctext,  
            padx=padx,       
            pady=pady, 
            relief=relief
        )
        btn.place(
            relx=xrel,
            rely=yrel
            )
        return btn

def createFrame(
    parent,
    bgcolor = style.verdelimaOscuro,
    xrel = 0.,
    yrel = 0.,
    relw = 0.,
    relh = 0.,
    cursor = "arrow"):
    f = tk.Frame(
        parent,
        background=bgcolor,
        cursor=cursor
        )
    
    f.place(
    relx=xrel,  
    rely=yrel,
    relwidth=relw,  
    relheight=relh,
    )
    return f