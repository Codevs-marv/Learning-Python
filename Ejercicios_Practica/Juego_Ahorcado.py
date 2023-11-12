# E J E R C I C I O
'''Implementa un juego de ahorcado donde el jugador tiene que adivinar una palabra oculta. Puedes generar palabras aleatorias o permitir que el usuario ingrese palabras. 
Añade funcionalidades como límites de intentos y la posibilidad de elegir categorías de palabras.'''

print('J U E G O   D E L   A H O R C A D O')
print("""INSTRUCCIONES:
    1. Escoge un nivel de dificultad
    2. Intenta adivinar la palabra, al comenzar se te darán pistas o no, dependiendo de la dificultad que hayas escogido
    3. Para escoger la posición donde pondrás la letra que consideras, inserta el número bajo la casilla.""")

while True:

    print('\n¿Empezamos?  :)')
    start = input('Ingresa "si" o "no"')
    start.lower() # convertir la entrada a minúsculas

    if start == 'no': # salir
        print('OK, Tómate tu tiempo ;)')
        break

    else: # comienza el juego
        print("""Escoge la dificultad:
            1. Muy fácil
            2. Fácil
            3. Media
            4. Difícil
            5. Avanzado""")
        dificultad = int(input('Ingresa el numero indicativo de dificultad: '))

        if (dificultad < 1) or (dificultad > 5):
            print('Nivel de dificultad no admitido, escoge de nuevo!')
        else:
            pass
        