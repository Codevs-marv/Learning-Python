# E J E R C I C I O
'''Implementa un juego de ahorcado donde el jugador tiene que adivinar una palabra oculta. Puedes generar palabras aleatorias o permitir que el usuario ingrese palabras. 
Añade funcionalidades como límites de intentos y la posibilidad de elegir categorías de palabras.'''

import random

nivel_1 = ['amor', 'paz', 'gato', 'perro', 'mundo', 'hola', 'lapiz', 'cielo', 'nube', 'agua', 'arbol', 'arroz', 'rojo', 'verde', 'azul', 'blanco', 'reloj', 'caja']
nivel_2 = ['python', 'programa', 'aleatorio', 'codigo', 'variable', 'busqueda', 'computo', 'edicion', 'operador', 'complejo', 'teclado', 'pantalla', 'elegante', 'elemento', 'secuencia']
nivel_3 = ['comentario', 'ingeniero', 'explorador', 'incendio', 'conexion', 'estudiante', 'implementacion', 'arquitecto', 'temporada', 'desarrollo', 'evaluacion', 'establecimiento', 'destornillador', 'herramientas']
nivel_4 = ['representante', 'espectacular', 'acondicionado', 'enciclopedia', 'extraordinario', 'desarrollador', 'contradictorio', 'administrador', 'inconveniente', 'anticonstitucional',
           'especificacion', 'diferenciacion', 'internacional', 'sobresaliente']
nivel_5 = ['quimericamente', 'anacronistico', 'inextricable', 'desacralizacion', 'obfuscacion', 'diseminacion', 'heterodoxamente', 'incorruptibilidad', 'indefatigable', 'inconmesurable',
           'desproporcionado', 'inefablemente', 'irrefutablemente', 'desenmarañamiento', 'intransigencia']

print('J U E G O   D E L   A H O R C A D O')
print("""INSTRUCCIONES:
    1. Escoge un nivel de dificultad
    2. Intenta adivinar la palabra, al comenzar se te darán pistas o no, dependiendo de la dificultad que hayas escogido
    3. Para escoger la posición donde pondrás la letra que consideras, inserta el número bajo la casilla.""")

while True:

    print('\n¿Empezamos?  :)')
    start = input('Ingresa "si" o "no"')
    start = start.lower()  # convertir la entrada a minúsculas

    if start == 'no':  # salir
        print('OK, Tómate tu tiempo ;)')
        break

    else:  # comienza el juego
        print("""Escoge la dificultad:
        1. Muy fácil
        2. Fácil
        3. Media
        4. Difícil
        5. Avanzado""")
        dificultad = int(input('Ingresa el numero indicativo de dificultad: '))

        if not (1 <= dificultad <= 5):
            print('Nivel de dificultad no admitido, escoge de nuevo!')
        else:
            pass

    completado = False  # inicializar la variable completado

    match dificultad:
        case 1:
            palabra_aleatoria = random.choice(nivel_1)
            adivinar = '_ ' * len(palabra_aleatoria)
            max_intentos = len(palabra_aleatoria) * 2     # cantidad de intentos 
            intentos = 0

            while not completado and intentos < max_intentos:
                print('\n¡Adivina la palabra!')
                print()
                print("{:>20}".format(adivinar))
                indices = " ".join(str(i) for i in range(len(palabra_aleatoria)))  # índices debajo de la palabra
                print('{:>19}'.format(indices))
                print('Inserta una letra (la que creas que va)')
                letra = input()
                letra = letra.lower()

                if not isinstance(letra, str):
                    print('El caracter ingresado no es una letra, inténtalo de nuevo!')
                    continue
                else:
                    print('Ingrese un índice (posicion donde quiere poner la letra)')
                    posicion = int(input())
                    palabra = list(palabra_aleatoria)
                    adivinar_lista = list(adivinar)

                    if letra == palabra[posicion]:  # comprobar si la letra ingresada coindice con la posición escogida
                        adivinar_lista[posicion] = letra
                        adivinar = " ".join(adivinar_lista)
                        completado = adivinar.replace(" ", "") == palabra_aleatoria  # verificar si la palabra ha sido adivinada
                    else:
                        print('La letra no coincide con la posición :(')
                        intentos += 1

