# E J E R C I C I O
''' Diseña un juego en el que el programa elija un número aleatorio y le pida al usuario que adivine ese número. Proporciona pistas (mayor/menor) y lleva un registro 
de cuántos intentos se necesitaron para adivinar el número.'''

import random

print('Este es un juego de adivinanza! Tienes 5 intentos para adivinar el número.')
print('¡BUENA SUERTE!')

# numero que se tiene que adivinar
numero_aleatorio = random.randint(1,10)

# contador de intentos 
intentos = 0

while intentos <= 4:
    if intentos == 0:
        print('Es un número entero entre 1 y 10 (incluidos). ¡Intenta adivinarlo!')
    else: 
        print('Intentalo de nuevo!')

    # numero elegido por el usuario
    num_usuario = int(input('Ingresa tu opción: '))

    if num_usuario == numero_aleatorio:
        print('¡ADIVINASTE! :)')
        break
    else:
        if intentos == 3:
            print('Esta es tu última oportunidad')   
        else:  
            print('Erraste :(')
    intentos += 1
