#  >>>  O P T I M I Z A R    C A D E N A S  <<<  #

#> Forma convencional
v = 'otro texto'
n = 10
print('Un texto', v, 'y un numero ', n)


#> Forma optimizada
c = 'Un texto {}  y un numero {}'.format(v,n)
print(c)

print('Un texto {1}  y un numero {0}'.format(v,n)) # cambiarle el orden con índices del .format()

print('Un texto {v}  y un numero {n}'.format(v=v,n=n)) # referenciar las variables

print('{v} {v} {v}'.format(v=v)) # por si se quiere repetir varias veces la misma referencia



#> ALINEAR, CENTRAR TEXTOS
# {ref variable: instrucciones} --->  {:>30}
print("{:>30}".format('palabra')) # alineamiento a la derecha en 30 caracteres

print("{:^30}".format('palabra')) # alineamiento al centro en 30 caracteres



#> TRUNCAMIENTO
print("{:.3}".format('palabra')) # mostrar las 3 primeras letras de la palabra

print("{:>30.3}".format('palabra')) # alineamiento a la derecha en 30 caracteres y truncamiento en3





#  >>> F O R M A T E O   D E   N U M E R O S  <<< #

# organizados a 4 digitos --> ":4"
print('{:4d}'.format(10))         #                10
print('{:4d}'.format(100))        # imprime:      100
print('{:4d}'.format(1000))       #              1000


# rellenados con ceros "0"
print('{:04d}'.format(10))       #               0010
print('{:04d}'.format(100))      # imprime:      0100
print('{:04d}'.format(1000))     #               1000


# Números deciamles
print('{:.3f}'.format(3.1415926))  # --> 3.142   (tres decimales)


print('{:7.3f}'.format(3.1415926))   #    3.142
print('{:7.3f}'.format(152.21))      #  152.210





#>> F - STRINGS
# forma aún mas simplificada

nombre = 'Marco'
cadena = f'Hola {nombre}'
print(cadena)  # --> Hola Marco

# Ejemplos:
#1
a, b = 10, 5
print( f'La suma de {a} y {b} es {a+b}')  # --> 15


#2
def func():
    return 'Pepe'

print( f'Hola {func()}') # --> Hola Pepe


#3
numeros = {'uno':1, 'dos':2, 'tres':3}
print( f"El números dos es {numeros['dos']}")


#> Alineamientos
texto = 'Hola mundo'

print( f'{texto:40}')  # a la izquierda 40 caracteres
print( f'{texto:>40}')  # a la derecha 40 caracteres
print( f'{texto:^40}')  # al centro 40 caracteres





#  >>>  F U N C I O N E S  <<< #

def numero():
    n = 2  # variable local

n = 3  # variable global


#> retorno
def palabra():
    return 'Esta es una cadena retornada'
    # todo lo que esté después del return no se ejecuta


def lista():
    return [1,2,3,4,5]

print(lista()) # ---> [1,2,3,4,5]
print(lista()[-1]) # ---> 5


def tupla():
    return 'cadena', [1,2,3], 20

print(tupla()) # ---> ('cadena', [1,2,3], 20) retorna una tupla

#> Asignacion multiple
a,b,c = tupla()
    # a = 'cadena'
    # b = [1,2,3]
    # c = 20


#> Argumentos Indeterminados

# posicion
def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(5,'Hola',[1,2,3,4,5]) # imprime cada argumento


def indeterminados_posicion(*args):
    for arg in args:
        print(arg) # imprime uno a uno cada argumento


# nombre
def indeterminados_nombre(**kwargs):
    print(kwargs)

indeterminados_nombre(n=5, c='Hola', l=[1,2,3,4,5]) # imprime un diccionario


def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print('Sumatorio indeterminado es:', t)

    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


