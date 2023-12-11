# Un SCRIPT es un guion de instrucciones guardadas en un fichero
# ¿Y si queremos una funcioón o clase en diferentes scripts?
# --> reutilización de código en módulos!


#  >>> M O D U L O S  <<< #

#> Módulos Estándar
"""
- copy
- collections
- datetime
- doctest y unittest
- html, xml y json
- pickle
- math
- re
- random
- socket
- sqlite3
- sys
- threading
- tkinter
"""



                                            #  >>>  C O L L E C T I O N S  <<<  #

# Counter(): Muestra un diccionario con la cantidad de veces que aparece un elemento
# .most_common(cantidad items): Saber cuales son los elementos mas comunes
# .keys(): Muestra los items sin repetirlos
# OrderedDict(): Crear diccionarios conservando el orden en que se añaden los items


from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

p = 'palabra'
Counter(p) 

animales = 'gato perro canario perro canario perro'
animales.split()

conteo = Counter(animales.split())
print(conteo)

# usar .most_common
conteo.most_common(1)




# Acceder a una clave que no existe
from collections import defaultdict

# defaultdict crea esa clave que no existe al intentar acceder a ella
d = {}
d = defaultdict(float)  

d['algo'] # 'algo' no exite y al intentar acceder a esa clave nos devuelve un valor float por defecto que será 0.0



# Diccionarios conservando el orden
from collections import OrderedDict

dic = OrderedDict() # se crea el dict

dic['uno'] = 'one'
dic['dos'] = 'two'
dic['tres'] = 'three'
dic['cuatro'] = 'four'
print(dic)




                                            #  >>>  D A T E T I M E  <<<  #

# .now() : Fecha y hora actual
# .isoformat(): Formato por defecto (fecha y hora)
# .strftime(): Formatear la fecha y hora personalmente
# .timedelta(): Sumar fechas (días,horas,minutos..etc) a la fecha actual



import datetime 

dt = datetime.datetime.now()
dt.year # año
dt.month # mes
dt.day # día
dt.hour # hora
dt.minute # min
dt.second # seg


formatop = dt.strftime("%A %d %B %Y, %I:%M")  # formato personalizado --> En ingles por defecto



# MODULO  >> L O C A L E <<

import locale
'proporciona funciones para trabajar con configuraciones de localización, como el formato de números, monedas y fechas, que pueden variar según la región y el idioma'

locale.setlocale(locale.LC_ALL, 'es')
formatop = dt.strftime("%A %d %B %Y, %I:%M")  # formato personalizado --> Ahora en ESPAÑOL

print('Fecha actual: ', formatop)


# sumar tiempo a la fecha y hora actual
t = datetime.timedelta(days=14, hours=4, seconds=1000)

dos_semanas_mas = (dt + t).strftime("%A %d %B %Y, %I:%M") # sumarle a la fecha actual el tiempo definido en t
print('Dentro de dos semanas será: ', dos_semanas_mas)




                                    #  >>>  M A T H  <<<  #

#> Modulo de funciones y métodos para trabajar con matemáticas

# round(): Redondeo normal
# .floor(): Funcion piso
# .ceil(): Funcion techo
# abs(): Valor absoluto
# sum(): Sumatorio
# fsum(): Suma decimal
# .trunc(): Eliminar la parte decimal
# .pow(): Elevar a un numero
# .sqrt(): Raiz cuadrada
# .pi : Trabajar con el valor exacto de pi
# .e : Valor exacto de e


import math

pi = 3.15159
round(pi) # redondea en base al decimal 5

n = [1,2,3]
sum(n) # --> 6

math.trunc(100.992920348) # --> 100








                                    #  >>> R A N D O M  <<<  #

#> Generar numeros y comportamientos al azar o aleatorios

import random

# .random(): Numero float aleatorio (0 - 1)
# .uniform(): Num float aleatorio entre 1 y 10
# .randrange(): Num entero aleatorio entre rango especificado
# .choice(): Elegir un elemento aleatorio
# .shuffle(): Baraja aleatoriamente los elementos de una lista o coleccion
# .sample(L,cant): Mostrar cantidad de elementos aleatorios de una lista


num = random.randrange(0,100,2)  # num int aleatorio entre 0 y 100 --> multiplos de 2

c = 'Hola mundo'
l = [1,2,3,4,5]

al = random.choice(c) # Elegir una letra aleatoria


