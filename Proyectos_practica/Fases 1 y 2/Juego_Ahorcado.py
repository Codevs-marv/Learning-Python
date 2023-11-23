# E J E R C I C I O
'''Implementa un juego de ahorcado donde el jugador tiene que adivinar una palabra oculta. Puedes generar palabras aleatorias o permitir que el usuario ingrese palabras. 
Añade funcionalidades como límites de intentos y la posibilidad de elegir categorías de palabras.'''

import random

nivel_1 = ['amor', 'paz', 'gato', 'perro', 'mundo', 'hola', 'lapiz', 'cielo', 'nube', 'agua', 'arbol', 'arroz', 'rojo', 'verde', 'azul', 'blanco', 'reloj', 'caja',
            'python', 'programa', 'aleatorio', 'codigo', 'variable', 'busqueda', 'computo', 'edicion', 'operador', 'complejo', 'teclado', 'pantalla', 'elegante', 'elemento', 'secuencia']
nivel_2 = ['comentario', 'ingeniero', 'explorador', 'incendio', 'conexion', 'estudiante', 'implementacion', 'arquitecto', 'temporada', 'desarrollo', 'evaluacion', 'establecimiento', 'destornillador', 'herramientas'
            'representante', 'espectacular', 'acondicionado', 'enciclopedia', 'extraordinario', 'desarrollador', 'contradictorio', 'administrador', 'inconveniente', 'anticonstitucional',
           'especificacion', 'diferenciacion', 'internacional', 'sobresaliente']
nivel_3 = ['quimericamente', 'anacronistico', 'inextricable', 'desacralizacion', 'obfuscacion', 'diseminacion', 'heterodoxamente', 'incorruptibilidad', 'indefatigable', 'inconmesurable',
           'desproporcionado', 'inefablemente', 'irrefutablemente', 'desenmarañamiento', 'intransigencia']

print('J U E G O   D E L   A H O R C A D O')
print("""INSTRUCCIONES:
    1. Escoge un nivel de dificultad
    2. Intenta adivinar la palabra, al comenzar se te darán pistas o no, dependiendo de la dificultad que hayas escogido
    3. Para escoger la posición donde pondrás la letra que consideras, inserta el número bajo la casilla.""")

while True:

    print('\n¿Empezamos?  :)')
    try:
        start = input('Ingresa "si" o "no"\n')
    except Exception as e:
        print(type.__name__, 'Ingresa una opción válida')
        continue
    start = start.lower()  # convertir la entrada a minúsculas

    if start == 'no':  # salir
        print('OK, Tómate tu tiempo ;)')
        break

    else:  # comienza el juego
        print("""Escoge la dificultad:
        1. Fácil
        2. Media
        3. Difícil
        """)
        try:
            dificultad = int(input('Ingresa el numero indicativo de dificultad: '))
        except ValueError:
            print('Ingrese una opción válida')
            continue

        if not (1 <= dificultad <= 3):
            print('Nivel de dificultad no admitido, escoge de nuevo!')
            continue

    completado = False  # inicializar la variable completado

    match dificultad:

        # Nivel Fácil
        case 1:
            Logrado = False
            palabra = random.choice(nivel_1)  # palabra al azar
            cont = len(palabra) + 3

            print('Adivina la palabra!\n')
            oculta = ['_'] * len(palabra)
            adiv = list(palabra)
            print(" ".join(oculta))

            while cont > 0 and not Logrado:
                try:
                    letra = input('Ingresa una letra (la que creas que va): ')
                except ValueError:
                    print('Debes ingresar una letra')
                    continue

                acertaste = False
                for i in range(len(adiv)):
                    if adiv[i] == letra:
                        oculta[i] = letra
                        acertaste = True

                if acertaste:
                    print(" ".join(oculta))
                    print()
                    
                    if "".join(oculta) == palabra:
                        Logrado = True
                        print('¡Felicidades! Has adivinado la palabra:', palabra)
                else:
                    print('No acertaste, pero aún tienes más intentos! ;)\n')

                cont -= 1

            if not Logrado and cont == 0:
                print(f'Has agotado tus intentos.\nLa palabra era: {palabra}')
                print('Buena suerte a la próxima ;-)')
        
        # Nivel Medio
        case 2:
            Logrado = False
            palabra = random.choice(nivel_2)  # palabra al azar
            cont = len(palabra) + 3

            print('Adivina la palabra!\n')
            oculta = ['_'] * len(palabra)
            adiv = list(palabra)
            print(" ".join(oculta))

            while cont > 0 and not Logrado:
                try:
                    letra = input('Ingresa una letra (la que creas que va): ')
                except ValueError:
                    print('Debes ingresar una letra')
                    continue

                acertaste = False
                for i in range(len(adiv)):
                    if adiv[i] == letra:
                        oculta[i] = letra
                        acertaste = True

                if acertaste:
                    print(" ".join(oculta))
                    print()
                    
                    if "".join(oculta) == palabra:
                        Logrado = True
                        print('¡Felicidades! Has adivinado la palabra:', palabra)
                else:
                    print('No acertaste, pero aún tienes más intentos! ;)\n')

                cont -= 1

            if not Logrado and cont == 0:
                print(f'Has agotado tus intentos.\nLa palabra era: {palabra}')

        # Nivel Difícil
        case 3:
            Logrado = False
            palabra = random.choice(nivel_3)  # palabra al azar
            cont = len(palabra) + 3

            print('Adivina la palabra!\n')
            oculta = ['_'] * len(palabra)
            adiv = list(palabra)
            print(" ".join(oculta))

            while cont > 0 and not Logrado:
                try:
                    letra = input('Ingresa una letra (la que creas que va): ')
                except ValueError:
                    print('Debes ingresar una letra')

                acertaste = False
                for i in range(len(adiv)):
                    if adiv[i] == letra:
                        oculta[i] = letra
                        acertaste = True

                if acertaste:
                    print(" ".join(oculta))
                    print()
                    
                    if "".join(oculta) == palabra:
                        Logrado = True
                        print('¡Felicidades! Has adivinado la palabra:', palabra)
                else:
                    print('No acertaste, pero aún tienes más intentos! ;)\n')

                cont -= 1

            if not Logrado and cont == 0:
                print(f'Has agotado tus intentos.\nLa palabra era: {palabra}')