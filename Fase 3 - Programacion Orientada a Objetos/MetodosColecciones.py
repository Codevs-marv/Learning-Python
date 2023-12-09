
# >>>  T O D O    S O B R E   C A D E N A S   <<< #

# .upper(): Convierte todo a mayúsculas
# .lower(): Convierte todo a minúsculas
# .capitalize(): Primera letra en mayúscula
# .title(): La primera letra en mayuscula de todas las palabras
# .count(): Contar la cantidad de veces que aparece un elemento
# .find(): Encontrar la primera ocurrencia de una subcadena dentro de una mas grande
# .rfind(): Encontrar la ultima aparición de una subcadena dentro de una mas grande
# .isdigit(): Si las letras que contiene son dígitos
# .isalnum(): Comproabr si la cadena es alfanumérica ---> NO contiene caracteres especiales
# .isalpha(): Comprobar si la cadena contiene caracteres alfabéticos solamente
# .islower(): Comprobar si todo está en minúsculas
# .isupper(): Comprobar si todo está en mayúsculas
# .istitle(): Comprobar si es un título
# .isspace(): Comprobar si todos los caracteres son espacios
# .startswith(): Comprobar si una cadena empieza con cierta cadena o una letra
# .endswith(): Comprobar si una cadena termina en cierta cadena o cierta letra
# .split(): Separar la cadena y convertirla en una lista
# .join(): Unir caracteres o cadenas
# .strip(): Borrar todos los espacios por defecto de una cadena de texto ó cierto caracter especifico (parametro)
# .replace(): Reemplazar cierto caracter o cadena por otro


n = '100'
c = 'ABC1239ps'
A = 'Hola mundo mundo mundo'
d = '    '

A.upper() # -> todo mayusculas
A.lower() # -> todo en minusculas
A.capitalize() # -> primera letra mayuscula
A.title() # -> primera letra de cada palabra mayuscula
A.count('o') # -> cuantas veces aparece la letra 'o'
A.find('mundo') # -> devuelve el el indice 5 (donde empieza la subcadena)
A.rfind('mundo') # -> ultima aparicion


n.isdigit() # -> True
c.isalnum() # --> True
c.isalpha() # --> False
c.islower() # --> False
d.isspace() # --> True

A.startswith('Hola') # --> True
A.startswith('H') # --> True
A.endswith('mundo') # -> True
A.endswith('m') # -> False

A.split() # --> ['Hola', 'mundo', 'mundo']
A.split()[0]  # --> ['Hola'] específicar el indice


' '.join('Hola')  # --> H o l a

'      marv   '.strip()  # --> 'marv'










#  >>>  T O D O    S O B R E   L I S T A S  <<<  #

# .append(): Añadir elemento
# .clear(): Vaciar la lista
# .extend(l2): Unir dos listas
# .count(): Contar cuantas veces aparece un elemento
# .index(item): Posicion donde aparece el item indicado
# .insert(indice,item): Añadir un elemento dentro de la lista en el indice indicado
# .pop(indice): ELimina el elemento con el indice indicado
# .remove(item): Elimina el item indicado
# .reverse(): Poner la lista del revés
# .sort(): Ordenar la lista en orden ascendente
# .sort(reverese=True): Ordena la lista en descendente


lista = [1,2,3,4,5]










#  >>>   T O D O    S O B R E    C O N J U N T O S   <<<  #

# .add(item): Añadir elemento
# .discard(item): Eliminar elemento 
# .copy(): Hacer una copia del conjunto para editarlo sin afectar el original
# .clear(): Vaciar el conjunto
# .isdisjoint(): Comprobar si dos conjuntos son disyuntos
# .issubset(): Comprobar si es un subconjuntos
# .superset(): Comprobar si es un superconjunto de otro



#>>> METODOS MAS AVANZADOS <<< #

# .union(): Unir dos conjuntos
# .update(): Une dos conjuntos y actualiza el primero
# .difference(): Obtener la diferencia entre dos conjuntos A - B (Elementos que estan en A pero no en B)
# .difference_upadate(): Actualizar y guardar la diferencia entre dos conjuntos
# .intersection(): interseca dos conjuntos
# .intersection_update(): Interseca dos conjuntos y guarda dicho resultado en el primero
# symmetric_difference(): Muestra los elementos diferentes de ambos conjuntos






c = set() # ---> crear conjunto

c.add(1)
c.add(2)
c.add(3)
c.discard(1)
c2 = c.copy() # copiar



c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

c1.isdisjoint(c2)

c1.union(c2) == c4 # True

c1.update(c2) # ---> c1 = {1,2,3,4,5}

c1.symmetric_difference(c2)  # --> {1,2,4,5} (el 3 lo excluye porque está en ambos conjuntos)













#  >>>  T O D O    S O B R E   D I C C I O N A R I O S  <<<  #

# .get(clave,msg): Devuelve el msg predefinido en el caso especifico en que se llame a esa clave
# .keys(): Devuelve una lista con las claves del diccionario
# .values(): Devuelve una lista con los valores del diccionario
# .items(): Devuelve una lista de tuplas con las claves y valores del dict
# .pop(clave): Eliminar elemento del diccionario haciendo referencia por su clave
# .clear(): Vacía el diccionario por completo



colores = {'amarillo': 'yellow', 'verde':'green','azul':'blue'}

colores['amarillo'] # --> 'yellow'
colores.get('negro','No se encuentra')

colores.keys()  # --> ['amarillo','verde','azul']



# mostrar claves
for c in colores:
    print(c)

# mostrar valores
for c in colores:
    print(colores[c])

# mostrar clave - valor
for c,v in colores.items():
    print(c,v)

