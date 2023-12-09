
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
