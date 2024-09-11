import threading
import tkinter as tk
import winsound


ikkuna=tk.Tk()

ikkuna.geometry("350x350+200+400")

Kernesti_sijainti_x=10
Ernest_sijainti_x=300

def kernesti_heittää():
    global Kernesti_sijainti_x

    

def ernesti_heittää():
    global Ernest_sijainti_x    

#osat/widgets

ernestinlohko=tk.Label(ikkuna,text="E")
ernestinlohko.place(x=Ernest_sijainti_x)

kernestinlohko=tk.Label(ikkuna,text="K")
kernestinlohko.place(x=Kernesti_sijainti_x)

ikkuna.mainloop()