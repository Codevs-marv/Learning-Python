# ¿QUÉ ES LA HERENCIA?
# --> La capacidad que tiene una clase de heredar métodos y atributos de otra, además de agregar nuevos o midificar los heredados


# CONTENIDO:
# -> Implementar la herencia
# -> Atributos y métodos heredados
# -> Qué es el polimorfismo
# -> Herencia múltiple


# >>>    H E R E N C I A   <<< #
# Superclase
class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.descripcion = descripcion
        self.nombre = nombre
        self.pvp = pvp
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return f"""
        REFERENCIA\t{self.referencia}
        NOMBRE\t\t{self.nombre}
        PVP\t\t${self.pvp}
        DESCRIPCION\t{self.descripcion}"""

# Subclase
class Adorno(Producto):
    pass


# Subclase
class Alimento(Producto):

    def __str__(self):
        return f"""
        REFERENCIA\t{self.referencia}
        NOMBRE\t\t{self.nombre}
        PVP\t\t${self.pvp}
        DESCRIPCION\t{self.descripcion}
        PRODUCTOR\t{self.productor}
        DISTRIBUIDOR\t{self.distribuidor}"""


# Subclase
class Libro(Producto):

    def __str__(self):
        return f"""
        REFERENCIA\t{self.referencia}
        NOMBRE\t\t{self.nombre}
        PVP\t\t${self.pvp}
        DESCRIPCION\t{self.descripcion}
        ISBN\t\t{self.isbn}
        AUTOR\t\t{self.autor}"""


ad = Adorno(2034, 'Vaso adornado', 15,'Vaso de porcelana adornado con arboles') # --> crear objeto (adorno)

al = Alimento(2035,'Botella Aceite de oliva Extra',5,"250 mL") # --> crear objeto (alimento)
al.productor = 'La Aceitera'
al.distribuidor = 'Distribuciones S.A'

lib = Libro(2036, 'Cocina Mediterránea', 9, 'Recetas sanas y buenas') # --> crear objeto (libro)
lib.isbn = '0-123456-78-9'
lib.autor = 'Juana Calderon'






#   >>> C L A S E S   H E R E D A D A S   Y   P O L I M O R F I S M O   <<<    #

# Superclase
class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.descripcion = descripcion
        self.nombre = nombre
        self.pvp = pvp
        self.productor = productor
        self.distribuidor = distribuidor

    def __str__(self):
        return f"""
        REFERENCIA\t{self.referencia}
        NOMBRE\t\t{self.nombre}
        PVP\t\t${self.pvp}
        DESCRIPCION\t{self.descripcion}"""

# Subclase
class Adorno(Producto):
    pass


# Subclase
class Alimento(Producto):

    def __str__(self):
        return f"""
        REFERENCIA\t{self.referencia}
        NOMBRE\t\t{self.nombre}
        PVP\t\t${self.pvp}
        DESCRIPCION\t{self.descripcion}
        PRODUCTOR\t{self.productor}
        DISTRIBUIDOR\t{self.distribuidor}"""


# Subclase
class Libro(Producto):

    def __str__(self):
        return f"""
        REFERENCIA\t{self.referencia}
        NOMBRE\t\t{self.nombre}
        PVP\t\t${self.pvp}
        DESCRIPCION\t{self.descripcion}
        ISBN\t\t{self.isbn}
        AUTOR\t\t{self.autor}"""


ad = Adorno(2034, 'Vaso adornado', 15,'Vaso de porcelana adornado con arboles') # --> crear objeto (adorno)

al = Alimento(2035,'Botella Aceite de oliva Extra',5,"250 mL") # --> crear objeto (alimento)
al.productor = 'La Aceitera'
al.distribuidor = 'Distribuciones S.A'

lib = Libro(2036, 'Cocina Mediterránea', 9, 'Recetas sanas y buenas') # --> crear objeto (libro)
lib.isbn = '0-123456-78-9'
lib.autor = 'Juana Calderon'


productos = [ad, al]
productos.append(lib)

for p in productos:
    print(p,'\n') # --> mostrar todos los detalles de cada producto

for i in productos:
    print(i.referencia, i.nombre) # --> mostrar detalles específicos de los productos

print('\n')


for p in productos:
    if (isinstance(p, Adorno)): # --->  isinstance(objeto, clase): verifica si un objeto es de cierta clase
        print(p.referencia, p.nombre)

    elif (isinstance(p, Alimento)):
        print(p.referencia, p.nombre, p.productor)

    elif (isinstance(p, Libro)):
        print(p.referencia, p.nombre, p.isbn)


# Funcion para rebajar precio
def Rebajar_Producto(p, rebaja):
    """Devuelve un producto con una rebaja en porcentaje de su precio"""

    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

al_rebajado = Rebajar_Producto(al, 10) # aplicar la funcion al producto 'al'
print(al_rebajado)



#>>> N O T A:
# Los objetos funcionan por referencia, es decir, cualquier cambio que se les haga así sea reasignandolos como una copia, se tomará ese cambio en el objeto original







# >>>  C O P I A R   O B J E T O S  <<< #

'Copiando los objetos de esta forma es la unica manera de crear cambios sobre la copia sin que se afecte el objeto original'

import copy

copia_adorno = copy.copy(ad) # --> se copió el objeto adorno
copia_adorno.pvp = 25  # --> cambiamos el precio de la copia

print(copia_adorno) # --> pvp = $25
print(ad) # --> pvp = $15 






#  >>>  H E R E N C I A   M U L T I P L E  <<<  #

class A:
    def __init__(self):
        print('Soy de clase A')
    
    def a(self):
        print('Este método lo heredo de A')

class B:
    def __init__(self):
        print('Soy de clase B')

    def b(self):
        print('Este método lo heredo de B')

class C(A,B):
    def c(self):
        print('Este método lo heredo de C')

