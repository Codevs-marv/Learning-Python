# E J E R C I C I O
#  Crea un programa que convierta entre diferentes unidades, como millas a kilómetros, grados Celsius a Fahrenheit, o cualquier otra conversión que elijas. Permite al usuario ingresar el valor y la unidad original,
#  y muestra el resultado en la unidad deseada.

print('CONVERSOR DE UNIDADES')
print()
print('¿Con qué unidades de medida quiere trabajar?')
print("""
    [1] Longitud
    [2] Temperatura
    [3] Masa
    [4] Tiempo
""")
opcion = int(input()) # unidad de medida a trabajar

match opcion:

    # Longitud
    case 1:
        print('Ingrese una cantidad: ')
        valor = float(input()) # --> valor a convertir

        # Unidad de medida inicial
        print('¿En qué unidades se encuentra el número ingresado?')
        print("""
            [1] Milimetros
            [2] Centimetros
            [3] Pulgadas (pulg)
            [4] Pies (ft)
            [5] Metros
            [6] Kilómetros
            [7] Millas
         """)
        und_inicial = int(input())

        # Unidad de medida que se desea otener
        print('¿A qué unidades quiere convertirlo?')
        print("""
            [1] Milimetros
            [2] Centimetros
            [3] Pulgadas (pulg)
            [4] Pies (ft)
            [5] Metros
            [6] Kilómetros
            [7] Millas
         """)
        convertir_a = int(input())
        
        match convertir_a:

            # convertir a milimetros
            case 1:
                result = 0

                if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 7: # comprobar opción
                    if und_inicial == 1:
                        result = valor
                        print(result)
                    elif (und_inicial == 2):
                        result = valor * 10
                        print(result)
                    elif (und_inicial == 3):
                        result = valor * 25.4
                        print(result)
                    elif (und_inicial == 4):
                        result = valor * 304.8
                        print(result)
                    elif (und_inicial == 5):
                        result = valor * 1000
                        print(result)
                    elif (und_inicial == 6):
                        result = valor * 1000000
                    else:
                        result = valor * 1609344
                        print(result)
                else:
                    print('La opción ingresada no es válida')
            
            # convertir a centimetros
            case 2:
                result = 0

                if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 7: # comprobar opción
                    if und_inicial == 2:
                        result = valor
                        print(result)
                    elif (und_inicial == 1):
                        result = valor / 10
                        print(result)
                    elif (und_inicial == 3):
                        result = valor * 25.4
                        print(result)
                    elif (und_inicial == 4):
                        result = valor * 30.48
                        print(result)
                    elif (und_inicial == 5):
                        result = valor * 100
                        print(result)
                    elif (und_inicial == 6):
                        result = valor * 100000
                    else:
                        result = valor * 160934.4
                        print(result)
                else:
                    print('La opción ingresada no es válida')
            
            # convertir a pulgadas
            case 3:
                result = 0

                if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 7: # comprobar opción
                    if und_inicial == 3:
                        result = valor
                        print(result)
                    elif (und_inicial == 1):
                        result = valor / 25.4
                        print(result)
                    elif (und_inicial == 2):
                        result = valor * 2.54
                        print(result)
                    elif (und_inicial == 4):
                        result = valor * 12
                        print(result)
                    elif (und_inicial == 5):
                        result = valor * 39.37
                        print(result)
                    elif (und_inicial == 6):
                        result = valor * 1000 * 39.37
                    else:
                        result = valor * 1609.344 * 39.37
                        print(result)
                else:
                    print('La opción ingresada no es válida')
            
            # convertir a pies
            case 4:
                result = 0

                if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 7: # comprobar opción
                    if und_inicial == 4:
                        result = valor
                        print(result)
                    elif (und_inicial == 1):
                        result = (valor / 1000) * 0.3048
                        print(result)
                    elif (und_inicial == 2):
                        result = valor / 30.48
                        print(result)
                    elif (und_inicial == 3):
                        result = valor / 12
                        print(result)
                    elif (und_inicial == 5):
                        result = valor * 0.3048
                        print(result)
                    elif (und_inicial == 6):
                        result = valor * 3280.84
                    else:
                        result = valor * 5280
                        print(result)
                else:
                    print('La opción ingresada no es válida')

            # convertir a metros
            case 5:
                result = 0

                if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 7: # comprobar opción
                    if und_inicial == 5:
                        result = valor
                        print(result)
                    elif (und_inicial == 1):
                        result = (valor / 1000) * 0.3048
                        print(result)
                    elif (und_inicial == 2):
                        result = valor / 30.48
                        print(result)
                    elif (und_inicial == 3):
                        result = valor / 12
                        print(result)
                    elif (und_inicial == 4):
                        result = valor * 0.3048
                        print(result)
                    elif (und_inicial == 6):
                        result = valor * 3280.84
                    else:
                        result = valor * 5280
                        print(result)
                else:
                    print('La opción ingresada no es válida')