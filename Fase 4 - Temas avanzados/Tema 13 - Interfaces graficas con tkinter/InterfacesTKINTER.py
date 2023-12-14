

                        # >>> I N T E R F A C E S    T K I N T E R  <<<  #

# Una interfaz es un medio visual a traves del que los usuarios pueden interactuar y realizar tareas


#> W I D G E T S:
# Representan los componentes gráficos en las interfaces y se gestionan formando jerarquías
# Tk
# Frame
# Label
# Entry
# text
# Button



#>> TK

# Tk(): Crear ventana principal (contenedor principal de otros widgets)
# .title(): Titulo de la ventana
# .mainloop(): Iniciar el bucle de eventos en la interfaz
# .iconbitmap(): Poner un icono en la barra de titulo
# .resizable(): Para redimensionar la ventana de la interfaz


from tkinter import *

root = Tk()
root.title('Hola mundo')
root.iconbitmap('hola.ico')
root.resizable(True, True)
root.mainloop()





#>> F R A M E S

# Frame(root): Crear el frame dentro de la raiz root
# .pack(): Colocar el widget en la ventana
# .config(): Configuraciones especificas para un widget

root = Tk()
root.title('Mi primer frame')
root.resizable(1,1)
root.iconbitmap('hola.ico')

frame = Frame(root)
frame.pack(fill='both',expand=1)
frame.pack(side='right') # side posiciona la raiz a alguno de los lados de la ventana
frame.config(width=480, height=320, cursor='pirate') # tamaño y cursor
frame.config(bd=25)
frame.config(bg='lightblue') # color
frame.config(relief='sunken')

root = Frame(root)
root.config(width=480, height=320, cursor='arrow') # tamaño y cursor
root.config(bd=15)
root.config(relief='ridge')
root.config(bg='lightblue') # color


# Inicia el bucle 
root.mainloop()







#>> L A B E L S

# Configuracion raiz
"""root = Tk()

# Configuracion de un marco
frame2 = Frame(root, width=480,height=320)
frame2.pack()

label = Label(frame2, text='¡Hola mundo!').pack()
Label(root, text='Otra etiqueta').pack()
Label(root, text='Última etiqueta').pack()
label.config(bg='green',fg='white',font=('Verdana',24))



# Bucle de la interfaz
root.mainloop()"""









#>> E N T R Y
# Es una entrada de texto


root = Tk()


# Entrada
entry = Entry(root)
entry.grid(row=0,column=1)
entry.config(justify='right') # entrada de text en el entry a la derecha

# Texto
label = Label(root, text='Nombre')
label.grid(row=0,column=0,sticky='e')


entry2 = Entry(root)
entry2.grid(row=1,column=1)
entry2.config(justify='center') # entrada de text en el entry en el centro
entry2.config(show='*') # ocultar lo que estamos ingresando

label2 = Label(root, text='Contraseña')
label2.grid(row=1,column=0,sticky='e')

root.mainloop()







#>> B U T T O N S

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set('')
    n2.set('')

root = Tk()

# variables
n1 = StringVar()
n2 = StringVar()
r = StringVar()

# Entradas
Label(root, text='Num 1').pack()
Entry(root, justify='center', textvariable=n1).pack() # 1er numero
Label(root, text='Num 2').pack()
Entry(root, justify='center', textvariable=n2).pack() # 2do numero

# Boton SUMAR
Button(root, text='Sumar', command=sumar).pack()

# Boton resta
Button(root, text='Restar', command=resta).pack()

# Boton producto
Button(root, text='Producto', command=producto).pack()


# Salida
Label(root, text='\nResult ->').pack()
Entry(root, justify='center', textvariable=r, state='disabled').pack() # result


root.mainloop()








#>> R A D I O   B U T T O N S

# Funcion para mostrar opcion seleccionada
def seleccionar():
    monitor.config(text='{}'.format(opcion.get()))



root = Tk()

opcion = IntVar()

Radiobutton(root, text='Opcion 1', variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text='Opcion 2', variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text='Opcion 3', variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

root.mainloop()