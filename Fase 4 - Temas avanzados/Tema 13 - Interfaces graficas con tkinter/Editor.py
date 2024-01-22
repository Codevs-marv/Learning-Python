from tkinter import *

def Nuevo():
    mensaje.set('Nuevo fichero')

def Abrir():
    mensaje.set('Abrir fichero')

def Guardar():
    mensaje.set('Guardar fichero')

def Guardar_como():
    mensaje.set('Guardar fichero como')




# Configuración de la raíz
root = Tk()
root.title('Mi Editor')


# Menú superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=Nuevo)
filemenu.add_command(label="Abrir", command=Abrir)
filemenu.add_command(label="Guardar", command=Guardar)
filemenu.add_command(label="Guardar como", command=Guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Arcivho")

# Caja de texto central
texto = Text(root)
texto.pack(fill=BOTH, expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas",12))

# Monitor inferior
mensaje = StringVar()
mensaje.set('Bienvenido a tu editor')
monitor = Label(root, textvar=mensaje, justify='left')
monitor.pack(side='left')


root.config(menu=menubar)

# Finalizar bucle de la app
root.mainloop()