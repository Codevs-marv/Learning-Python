

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
root = Tk()

# Configuracion de un marco
frame2 = Frame(root, width=480,height=320)
frame2.pack()

label = Label(frame2, text='¡Hola mundo!').pack()
Label(root, text='Otra etiqueta').pack()
Label(root, text='Última etiqueta').pack()
label.config(bg='green',fg='white',font=('Verdana',24))



# Bucle de la interfaz
root.mainloop()









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

# Vaciar la opcion seleccionada
def reset():
    opcion.set(None)
    monitor.config(text='')

root = Tk()

opcion = IntVar() # opcion seleccionada

Radiobutton(root, text='Opcion 1', variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text='Opcion 2', variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text='Opcion 3', variable=opcion, value=3, command=seleccionar).pack()

monitor = Label(root)
monitor.pack()

Button(root, text='Reiniciar', command=reset).pack()

root.mainloop()









#>> C H E C K   B U T T O N S

# onvalue : Valor cuando esta marcado
# offvalue: Valor cuando está desmarcado

def seleccionar():
    cadena = ''
    if (leche.get()):
        cadena += 'Con leche'
    else:
        cadena += 'Sin leche'

    if (azucar.get()):
        cadena += ' y con azucar'
    else:
        cadena += ' y sin azucar'
    
    monitor.config(text=cadena)

root = Tk()
root.title('Cafetería')
root.config(bd=15)

# variables que capturan la opcion escogida ---> (1=si , 0=no)
leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file='imagen.gif')
Label(root, image=imagen).pack(side='left')

frame = Frame(root)
frame.pack(side='right')

Label(frame, text='¿Como quieres el café?').pack(anchor='w')
Checkbutton(frame, text='Con leche', variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor='w')
Checkbutton(frame, text='Con azucar', variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor='w')

monitor = Label(frame)
monitor.pack()

root.mainloop()








#>> M E N U S

# El menú no se empaqueta (.pack()) sino que se añade manualmente al root 

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

# Menú Archivo
filemenu = Menu(menubar, tearoff=0)
#Sub-menús
filemenu.add_command(label='Nuevo')
filemenu.add_command(label='Abrir')
filemenu.add_command(label='Guardar')
filemenu.add_command(label='Cerrar')
filemenu.add_separator()
filemenu.add_command(label='Salir', command=root.quit)


# Menú Editar
editmenu = Menu(menubar, tearoff=0)
# Sub-menús
editmenu.add_command(label='Cortar')
editmenu.add_command(label='Copiar')
editmenu.add_command(label='Pegar')


# Menú Ayuda
helpmenu = Menu(menubar, tearoff=0)
# Sub-menús
helpmenu.add_command(label='Ayuda')
helpmenu.add_separator()
helpmenu.add_command(label='Acerca de...')


menubar.add_cascade(label='Archivo', menu=filemenu)
menubar.add_cascade(label='Editar', menu=editmenu)
menubar.add_cascade(label='Ayuda', menu=helpmenu)

root.mainloop()









#>> P O P U P S
# (Ventanas emergentes)

# BASICAS
from tkinter import messagebox 

root = Tk()

def test():
    messagebox.showinfo('Titulo','Hola que mas') # ventana de informacion
    messagebox.showwarning('ALERTA','Virus en el sistema') # ventaa de advertencia
    messagebox.showerror('ERROR','El programa no funciona') # ventana de error

    resultado = messagebox.askquestion('Salir','¿Estás seguro que quieres salir sin guardar?')
    if resultado == 'yes':
        root.destroy() # cerrar el programa

    resultado = messagebox.askokcancel('Salir','¿Sobreescribir el fichero actual?')
    if resultado: # if true
        root.destroy()

    resultado = messagebox.askretrycancel('Reintentar', 'No se puede conectar')
    if not resultado: # if false
        root.destroy()

Button(root, text='Click', command=test).pack()






# AVANZADAS

# initialdir: Especificar donde se abre por defecto al 'examinar' los archivos del pc
# filetypes: Filtro por tipo de archivo al examinar las carpetas del pc

from tkinter import colorchooser # --> colores
from tkinter import filedialog  # --> 


# Funcion para elegir un color
def elegir_color():
    color = colorchooser.askcolor(title='Elige un color') # abre una ventana para esocoger un color


# Funcion para examinar las carpetas del pc
def Examinar():
    ruta = filedialog.askopenfilename(title='Abrir un archivo', initialdir='C:/',   # abrir las carpetas del pc
                                    filetypes=(('Archivos de texto', '*.txt'),
                                               ('Archivos de texto avanzado', '*.txt2'),
                                               ('Todos los archivos', '*.*'))) 
    
    # en 'ruta' se guarda la ruta del archivo que se abre


# Funcion para guardar un archivo en ruta especificada
def guardar_archivo():
    archivo = filedialog.asksaveasfile(title='Guardar un archivo', mode='a+', defaultextension='.txt')
    if archivo is not None:
        archivo.write('Hola!')
        archivo.close()




Button(root, text='Color', command=elegir_color).pack()
Button(root, text='Examinar', command=Examinar).pack()
Button(root, text='Guardar', command=guardar_archivo).pack()

root.mainloop()