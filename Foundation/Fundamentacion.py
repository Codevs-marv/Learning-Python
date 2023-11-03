print("esto es un\nsalto de linea")  # \n hace un salto de linea
print(r"C:\nombre\archivo")          # r al principio del string omite las funciones especiales 



#  >>>    S T R I N G S    <<<  #

# NOTA: Los Strings no son mutables

# P Y T H O N
# 0 1 2 3 4 5
palabra = "Python"  
palabra[0]                           # letra P (índices del string)
palabra[0:2]   # --> "Py"            # se omite el índice final 
palabra[2:-1]  # --> "tho"
palabra[2:]   # --> #thon            # con el segundo valor vacío muestra el último índice

palabra[0] = "N"  # --> error        # no se puede reasignar caracteres en un string
palabra = "N" + palabra[1:]  # --> Nython      # forma de cambiar la primera letra del string

palabra[::-1]  # --> nohtyP           # Invierte el orden del string

len()  # Para saber el tamaño
len(palabra)  # --> devuelve la cantidad de caracteres del string




#  >>>    L I S T A S    <<<  #

# NOTA: Las listas si son mutables

numeros = [1,2,3,4,5]
lista = [1, "hola", -15, 3.14]  #  Una lista puede contener distintos tipos de datos
lista[-2:]  # --> [3.14, -15] 
numeros + [6,7,8,9]  # --> [1,2,3,4,5,6,7,8,9]      concatenar dos listsa

pares = [2,4,5,8,10]
pares[3] = 6   # reasignar el valor del ítem en la lista

#  .append() :  añadir elemento al final de la lista
pares.append(12)  # --> [...8,10,12]

# .index() : para buscar elemento y posición
pares.index(5)  # --> retorna 2 (indice del elemento)

len(pares)  # --> 6

# Listas Anidadas

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]   # Una lista que contiene a otras listas
r[0][0]   # primer elemento de la primera lista dentro de r




#  >>>    L E C T U R A   P O R   T E C L A D O   <<<  #

valor = input("Introduce un valor: ")  # asignar un valor a una variable desde una entrada de teclado
    # --> se introduce:  100
    # No se puede operar como número porque toda entrada por teclado se toma como STRING

valor = int(valor)  # cambiamos el tipo de dato 
valor += 400  # --> 500 

value = float( input("Introduce un valor entero o decimal: "))   #  Acortar expresiones  (menos líneas de código)




#  >>>    O P E R A D O R E S    <<<  #

#> Lógicos:
    # Verdadero (True) y Falso (False)  <-- Veracidad de una sentencia o expresión
    # not (negación)
    # and (conjunción)
    # or (disyunción)
a = 13
(a > 10) and (a < 20)  # --> True
("H" == "H") or (1 > 2) # --> True  (si al menos uno es verdad entonces es True)
"Estoy vivo"  # --> True
    # 1 + 1 = 3 ---> False

#> Relacionales:
    # Son comparadores --> 
3 == 3  # --> Igual que..
2 != 3  # --> distinto de..
5 > 1  # --> mayor que
2 < 6  # --> menor que
3 >= 2  # --> mayor o igual 
1 <= 3  # --> menor o igual 

a = 10
b = 5
a > b  # --> True
b != a # --> True
b == a*2  # --> True
"Hola" == "Hola"  # --> True
c = "Hola"
c[0] == "H"  # --> True





#  >>>    C O N T R O L A N D O    E L    F L U J O    <<<  #

#> Condicionales:
    # if : si se cumple algo
    # else : sino se cumple algo
    # elif : sino si...

if True:
    print("Se cumple la condición")

else:
    print("No se cumple la condición")

# Example:
a = 5
if a == 2:               # --> si la condición es falsa, se omite automaticamente las expresiones indentadas dentro de dicha condición
    print("a vale 2")
else:
    print("a es diferente de 2")


n = int(input("Ingrese un número entero: "))
if n % 2 == 0:
    print(n, " es un número par")
else:
    print(n, " es impar")

if True:
    pass  # --> Bloque de code vacío, si se cumple la condición se almacena el True pero no se hace nada


#> match :  Funciona de manera similar a una serie de declaraciones if...elif...else, pero es más conciso y legible.
# case patronN if condicion:  Puedes incluir una condición después de un patrón para realizar una comprobación adicional antes de ejecutar el código.
# case _:  El patrón _ es un patrón comodín que coincide con cualquier cosa. Se utiliza como un caso de "por defecto" cuando ninguno de los patrones anteriores coincide.

def obtener_tipo(valor):
    match valor:
        case str(s) if s.isnumeric():
            return "Es un número como cadena"
        case int():
            return "Es un número entero"
        case float(f) if f.is_integer():
            return "Es un número decimal que parece entero"
        case float():
            return "Es un número decimal"
        case _:
            return "No es un número"

resultado = obtener_tipo(42)
print(resultado)



#> BUCLE WHILE:
# --> mientras..
# Iterar: repetir algo varias veces

c = 0
while c < 5:
    c += 1
    print("c vale ", c)
else:                             # --> se puede usar un "else" en caso de que el while no se cumpla
    print("Se ha completado toda la iteración y c vale ", c) 



#> Break 
c = 0
while c < 5:
    c += 1
    if (c == 2):
        print("Rompemos el bucle cuando c vale ", c)
        break           # ---> terminar el bucle
    print("c vale ", c)
else:                            
    print("Se ha completado toda la iteración y c vale ", c)


#> Continue
c = 0
while c < 5:
    c += 1
    if (c == 2):
        print("Rompemos el bucle cuando c vale ", c)
        continue           # ---> omitir la iteración en curso y continuar con la siguiente
    print("c vale ", c)
else:                            
    print("Se ha completado toda la iteración y c vale ", c)


#> Bucle infinito
while (True):
    print("El bucle se repetirá infinitamente")
    break


#> Recorrer Listas
numbers = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while indice < len(numbers):
    print(numeros[indice])


#> Bucle FOR
for number in numbers:  # --> itera sobre cada elemento de la lista
    print(number)  

indice = 0
numeros = [1,2,3,4,5,6,7,8,9,10]

# modificar los valores de la lista iterando sobre los indices de cada elemento
for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)



#>>> Enumerate
# sintaxis ---> enumerate(iterable, start=0)
# iterable: El iterable (lista, tupla, cadena, etc.) que deseas recorrer y enumerar.
# start (opcional): Un número entero que representa el valor inicial del contador. Por defecto, comienza en 0.
# --> (posición, elemento) <-- forma en que trabaje enumerate()


for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
print(numeros)  # --> [10,20,30,40,50,60,70,80,90,100]




#> Bucles anidados

tabla = [
    [0,0,0],
    [1,1,1],
    [2,2,2]
]

for fila in tabla:
    for columna in fila:
        print(columna, end=" ")
    print()

for i,fila in enumerate(tabla):
    for j,columna in enumerate(fila):
        print(tabla[i][j], end=" ")
    print()




        #>>> T U P L A S    <<<#

# No se pueden modificar sus elementos
tupla = (1, "Hola", [1,2,3], -50)
tupla[2:]  # --> ([1,2,3], -50)
tupla[2][-1] # --> 3

# .index() : para buscar elemento y posición
tupla.index("Hola") # --> 1 (índice)

# .count() : contar cuantas veces aparece un elemento
tupla.count(-50) # --> 1 (aparece una vez)




#  >>>    C O N J U N T O S    <<<  #

# .add() : agregar elemento 
# .remove() : eliminar elemento  --> si el elemento no está genera ERROR
# .discard() : eliminar elemento sin generar error
# .union() : union de conjuntos
# .intersection() : intersección de conjuntos
# .difference() : diferencia de conjuntos
# .update() : añadir varios elementos en la misma liena

conjunto = set() # conjunto vacío
conjunto = {1,2,"Aloha",4,3,"Hola"}

grupo = {'Hector', 'Juan', 'Mario'}
'Hector' in grupo # --> True    (comprobar si el elemento está en el conjunto)

lista = [1,2,3,3,2,1]

# se quiere eliminar los elementos repetidos de la lista
lista = list( set(lista) )





#  >>>    D I C C I O N A R I O S    <<<  #

#  clave : valor
# del() : eliminar (clave:valor) del diccionario
# mi_diccionario["género"] = "masculino"  : agregar cosas
# .keys() : obtener lista de claves del diccionario
# .values() : obtener lista de valores
# .items() : obtener lista de pares (clave:valor)


colores = {'amarillo':'yellow','azul':'blue','rojo':'red','blanco':'white'}

colores['amarillo']  # --> 'yellow'
colores['azul'] = 'BLUE'  # redefinir el valor de una clave

# iterar en el dict
for clave,valor in colores.items():
    print(clave, valor)


# crar una lista de personajes con sus características
personajes = []
p1= {'nombre':'Gandalf','clase':'mago','raza':'humano'}
personajes.append(p1) # añadir personaje a la lista de personajes

