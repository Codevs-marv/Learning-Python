# E J E R C I C I O
'''Crea un programa que genere contraseñas seguras basadas en criterios específicos (longitud, caracteres especiales, letras mayúsculas y minúsculas, números, etc.). 
Puedes permitir que los usuarios personalicen los criterios o generar automáticamente contraseñas seguras.'''

print('G E N E R A D O R   D E   C O N T R A S E Ñ A S')
print("""> Con al menos 8 caracteres
      > Mayúsculas
      > Incluye letras y números
      > Caracteres especiales (# ! / $)
      """)

import random

letras_mayusculas = [chr(i) for i in range(65, 91)]  # Del código ASCII 65 (A) al 90 (Z)
letras_minusculas = [chr(i) for i in range(97, 123)]  # Del código ASCII 97 (a) al 122 (z)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
especiales = ['!', '#', '%', '/', '¡', '-', '.', '_', '*']

while True:
    print('Escoge una opción:\n[1] Generar contraseña\n[2] Salir')

    try:
        opcion = int(input())
    except ValueError:
        print('Opción no válida. Ingresa el número de la opción')
        continue

    if opcion == 1:
        print('Generando contraseña...')
        contrasena = []

        for i in range(3):
            contrasena.append(random.choice(letras_minusculas))
            contrasena.append(random.choice(letras_mayusculas))
            contrasena.append(random.choice(numeros))
            contrasena.append(random.choice(especiales))

        random.shuffle(contrasena)  # Mezcla la contraseña generada
        generated = ''.join(map(str, contrasena))  # Contraseña generada
        print(f'Contraseña generada: --> {generated}')
    elif opcion == 2:
        print('Saliste del programa')
        break
    else:
        print('Opción no válida')
