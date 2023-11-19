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