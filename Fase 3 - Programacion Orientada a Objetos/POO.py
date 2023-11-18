# La clase es como un molde para crear objetos


# >>> I N S T A N C I A C I O N <<< #
# Crear un objeto a partir de su clase
class Galleta():
    pass

una_galleta = Galleta() 
otra_galleta = Galleta() # --> objeto de clase galleta

type(una_galleta) # --> __main__.Galleta





# >>> A T R I B U T O S  <<< #
class Galleta_Noel():
    pass

galleta_salada = Galleta_Noel()
galleta_salada.sabor = 'Salado'
galleta_salada.color = 'Beige'
print(galleta_salada.sabor) # ---> salado


class Galletas():
    chocolate = False

galleta1 = Galletas()
galleta1.chocolate  # -->  False


#>> Especificar atributos de manera eficiente

# MÉTODO: es una función dentro de una clase
# __init__()
# self

class Galletas():
    chocolate = False

    # 1er método
    def __init__(self):
        print('Se acaba de crear una galleta')

    # 2do método
    def chocolatear(self):
        self.chocolate = True
    
    # 3er método
    def tiene_chocolate(self):
        if (self.chocolate):
            print('Galleta con chocolate :)')
        else:
            print('Galleta sin chocolate :(')

g = Galletas()
g.tiene_chocolate() # --> Galleta sin chocolate :(
g.chocolatear()
g.chocolate # --> True
g.tiene_chocolate() # --> Galleta con chocolate :)




# Agregar mas Atributos

class Galletas():
    chocolate = False

    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print(f'Se acaba de crear una galleta {sabor} {forma}')

    def chocolatear(self):
        self.chocolate = True
    
    def tiene_chocolate(self):
        if (self.chocolate):
            print('Galleta con chocolate :)')
        else:
            print('Galleta sin chocolate :(')

g = Galletas('salada', 'cuadrada') # se crea un objeto galleta con atributos sabor y forma




# Galleta sin atributos

g = Galletas() # --> genera error (necesita pasarle argumentos)

def __init__(self, sabor=None, forma=None): # valor por defecto None
        self.sabor = sabor
        self.forma = forma

        if sabor != None or forma != None:
            print(f'Se acaba de crear una galleta {sabor} {forma}')
        else:
            print('Se acaba de crear una galleta sin sabor ni forma')






# >>>  M É T O D O S   E S P E C I A L E S  <<< #

class Pelicula():
    # constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película', self.titulo)

    # destructor de clase
    def __del__(self):
        print('Se está borrando la película', self.titulo)

    # redefinir el método string
    def __str__(self):
        return f'{self.titulo} lanzada en {self.lanzamiento} con una duración de {self.duracion} minutos'
    
    # redefinir el método len
    def __len__(self):
        return self.duracion
    
peli = Pelicula('El Padrino', 175, 1972)






# >>> O B J E T O S   D E N T R O   D E   O B J E T O S  <<< #

class Pelicula:

    # constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'
    

class Catalogo:
    peliculas = []

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):
        self.peliculas.append(p)
    
    def mostrar(self):
        for p in self.peliculas:
            print(p)

# crear peliculas

p1 = Pelicula('El Padrino', 175, 1972)
p2 = Pelicula('Avatar', 143, 2009)
c = Catalogo([p1,p2]) # agregar las pelis al catálogo
c.agregar(Pelicula('Fast and Furious 1', 165, 2007)) # agregar película con el método

c.mostrar() # --> muestra las peliculas del catálogo con el formato dado en "def __str__" 
# porque print() internamente usa str para obtener una representación en cadena







# >>> E N C A P S U L A C I O N    D E    A T R I B U T O S    Y    M E T O D O S  <<< #

'''La encapsulación en programación orientada a objetos (POO) es un concepto que se refiere a la restricción del acceso a ciertos componentes internos de un objeto. 
En Python, la encapsulación se logra principalmente mediante la convención de nombres y el uso de atributos y métodos privados.'''

class Ejemplo:

    # atributo privado
    __atributoPrivado__ = 'Soy un atributo inalcanzable'

    # método privado
    def __MetodoPrivado__(self):
        print('Soy un método inalcanzable')
    
    def MetodoPublico(self):
        return self.__MetodoPrivado()

e = Ejemplo() # crear objeto
e.MetodoPublico() # se ejecuta el método privado a partir del público

