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
