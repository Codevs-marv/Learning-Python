

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





#>> FRAMES

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







#>> LABELS

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









#>> ENTRY
# Es una entrada de texto


root = Tk()


# Entrada
entry = Entry(root)
entry.grid(row=0,column=1)

# Texto
label = Label(root, text='Nombre')
label.grid(row=0,column=0,sticky='e')



entry2 = Entry(root)
entry2.grid(row=1,column=1)

label2 = Label(root, text='Apellidos')
label2.grid(row=1,column=0,sticky='e')

root.mainloop()