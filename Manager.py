import tkinter as tk
from constants import style  
from tkinter import messagebox
import sys

class Manager(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.title(style.titulo)  
        self.geometry(style.windowSize)  
        self.minsize(width=1300, height=800)
    
    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Seguro que quieres salir?"):
            self.destroy()
            sys.exit()

   


