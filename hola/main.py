import tkinter as tk
import time
from PIL import Image, ImageTk

wn = tk.Tk()

fondo = Image.open("cr7.jpg")
photo = ImageTk.PhotoImage(fondo)

backGround = tk.Label(wn, image = photo)
backGround.place(x=0, y=0, relwidth=1, relheight=1)

bFoto = Image.open("cr7btn.jpg")
bFoto = bFoto.resize((100,100))
cr7 = ImageTk.PhotoImage(bFoto)



wn.title("hola")
etiqueta = tk.Label(wn, text="Hola")
etiqueta.pack()
def accion():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    wn.after(1000, accion)

btn = tk.Button(wn,image=cr7,command=accion)
btn.pack()

wn.geometry("400x400")



wn.mainloop()

