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

