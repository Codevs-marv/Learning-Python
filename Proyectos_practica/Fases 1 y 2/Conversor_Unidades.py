# E J E R C I C I O
#  Crea un programa que convierta entre diferentes unidades, como millas a kilómetros, grados Celsius a Fahrenheit, o cualquier otra conversión que elijas. Permite al usuario ingresar el valor y la unidad original,
#  y muestra el resultado en la unidad deseada.

print('CONVERSOR DE UNIDADES')
print()

while True:
    print('¿Con qué unidades de medida quiere trabajar?')
    print("""
        [1] Longitud
        [2] Temperatura
        [3] Tiempo
    """)
    try:
        opcion = int(input()) # unidad de medida a trabajar
    except ValueError:
        print('Por favor, ingrese un número válido')
        continue

    match opcion:

        #> LONGITUD
        case 1:
            print('Ingrese una cantidad: ')
            try:
                valor = float(input()) # --> valor a convertir
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

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
            try:
                und_inicial = int(input())
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

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
            try:
                convertir_a = int(input())
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue
            
            if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 7:
                match convertir_a:
                    
                    # convertir a milimetros
                    case 1:
                        result = 0

                        if und_inicial == 1:
                            result = valor
                        elif (und_inicial == 2):
                            result = valor * 10
                        elif (und_inicial == 3):
                            result = valor * 25.4
                        elif (und_inicial == 4):
                            result = valor * 304.8
                        elif (und_inicial == 5):
                            result = valor * 1000
                        elif (und_inicial == 6):
                            result = valor * 1000000
                        else:
                            result = valor * 1609344
                        
                        print(f'El resultado es: {result}mm')
                        break
                    
                    # convertir a centimetros
                    case 2:
                        result = 0

                        if und_inicial == 2:
                            result = valor
                        elif (und_inicial == 1):
                            result = valor / 10
                        elif (und_inicial == 3):
                            result = valor * 25.4
                        elif (und_inicial == 4):
                            result = valor * 30.48
                        elif (und_inicial == 5):
                            result = valor * 100
                        elif (und_inicial == 6):
                            result = valor * 100000
                        else:
                            result = valor * 160934.4
                        
                        print(f'El resultado es: {result}cm')
                        break
                    
                    # convertir a pulgadas
                    case 3:
                        result = 0

                        if und_inicial == 3:
                            result = valor
                        elif (und_inicial == 1):
                            result = valor / 25.4
                        elif (und_inicial == 2):
                            result = valor * 2.54
                        elif (und_inicial == 4):
                            result = valor * 12
                        elif (und_inicial == 5):
                            result = valor * 39.37
                        elif (und_inicial == 6):
                            result = valor * 1000 * 39.37
                        else:
                            result = valor * 1609.344 * 39.37
                        
                        print(f'El resultado es: {result}pulg')
                        break
                    
                    # convertir a pies
                    case 4:
                        result = 0

                        if und_inicial == 4:
                            result = valor
                        elif (und_inicial == 1):
                            result = (valor / 1000) * 0.3048
                        elif (und_inicial == 2):
                            result = valor / 30.48
                        elif (und_inicial == 3):
                            result = valor / 12
                        elif (und_inicial == 5):
                            result = valor * 0.3048
                        elif (und_inicial == 6):
                            result = valor * 3280.84
                        else:
                            result = valor * 5280
                        
                        print(f'El resultado es: {result}ft')
                        break


                    # convertir a metros
                    case 5:
                        result = 0

                        if und_inicial == 5:
                            result = valor
                        elif (und_inicial == 1):
                            result = valor / 1000
                        elif (und_inicial == 2):
                            result = valor / 100
                        elif (und_inicial == 3):
                            result = valor * 0.0254
                        elif (und_inicial == 4):
                            result = valor * 0.3048
                        elif (und_inicial == 6):
                            result = valor * 1000
                        else:
                            result = valor * 1609.34
                        
                        print(f'El resultado es: {result}m')
                        break

                    # convertir a km
                    case 6:
                        result = 0

                        if und_inicial == 6:
                            result = valor
                        elif (und_inicial == 1):
                            result = valor / 1000000
                        elif (und_inicial == 2):
                            result = valor / 100000
                        elif (und_inicial == 3):
                            result = (valor * 0.0254) * 0.001
                        elif (und_inicial == 4):
                            result = (valor * 0.3048) * 0.001
                        elif (und_inicial == 5):
                            result = valor / 1000
                        else:
                            result = valor * 1.60934
                        
                        print(f'El resultado es: {result}km')
                        break

                    # convertir a millas
                    case 7:
                        print('Por el momento no está disponible esta opción')
                        break
            else:
                print('ERROR > Opción ingresada no válida')
                break


        #> TEMPERATURA
        case 2:
            print('Ingrese una cantidad: ')
            try:
                valor = float(input()) # --> valor a convertir
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

            # Unidad de medida inicial
            print('¿En qué unidad de temperatura está el valor ingresado?')
            print("""
                [1] Grados Celsius (°C)
                [2] Grados Fahrenheith (°F)
                [3] Grados Kelvin (K)
            """)
            try:
                und_inicial = int(input())
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

            # Unidad de medida que se desea otener
            print('¿A qué unidades quiere convertirlo?')
            print("""
                [1] Grados Celsius (°C)
                [2] Grados Fahrenheith (°F)
                [3] Grados Kelvin (K)
            """)
            try:
                convertir_a = int(input())
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

            if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 3:
                match convertir_a:
                    
                # convertir a °C
                    case 1:
                        resultado = 0

                        if und_inicial == 1:
                            resultado = valor
                        elif und_inicial == 2:
                            resultado = (valor - 32) * (5/9)
                        else:
                            resultado = valor - 273.15
                                            
                        print('El resultado es: ', f'{resultado}°C')
                        break

                    # convertir a °F
                    case 2:
                        resulta = 0

                        if und_inicial == 2:
                            resulta = valor
                        elif und_inicial == 1:
                            resulta =  (valor * (9/5)) + 32
                        else:
                            resulta = (valor - 273.15) * (9/5) + 32

                        print('El resultado es: ', f'{resulta}°F')
                        break

                    # convertir a K
                    case 3:
                        res = 0

                        if und_inicial == 3:
                            res = valor
                        elif und_inicial == 1:
                            res = valor + 273.15
                        else:
                            res = (valor - 32) * (5/9) * 273.15

                        print('El resultado es: ', f'{res}°K')
                        break
            else:
                print('ERROR > Opción ingresada no válida')
                break


        #> TIEMPO
        case 3:
            print('Ingrese una cantidad: ')
            try:
                valor = float(input()) # --> valor a convertir
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

            # Unidad de medida inicial
            print('¿En qué unidad del tiempo está el valor ingresado?')
            print("""
                [1] Segundos (seg)
                [2] Minutos (min)
                [3] Horas (h)
                [4] Dias 
            """)
            try:
                und_inicial = int(input())
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue

            # Unidad de medida que se desea otener
            print('¿A qué unidades quiere convertirlo?')
            print("""
                [1] Segundos (seg)
                [2] Minutos (min)
                [3] Horas (h)
                [4] Dias
            """)
            try:
                convertir_a = int(input())
            except ValueError:
                print('Por favor, ingrese un número válido')
                continue
        
            if 1 <= und_inicial <= 7 and 1 <= convertir_a <= 4:
                    
                match convertir_a:
                
                    # convertir a segundos
                    case 1:
                        resul = 0

                        if und_inicial == 1:
                            resul = valor
                        elif und_inicial == 2:
                            resul = valor * 60
                        elif und_inicial == 3:
                            resul = valor * 3600
                        else:
                            resul = valor * 86400

                        print(f'El resultado es: {resul}seg')
                        break

                    # convertir a minutos
                    case 2:
                        resul = 0

                        if und_inicial == 2:
                            resul = valor
                        elif und_inicial == 1:
                            result = valor / 60
                        elif und_inicial == 3:
                            resul = valor * 60
                        else:
                            resul = valor * 1440

                        print(f'El resultado es: {resul}min')
                        break

                    # convertir a horas
                    case 2:
                        resul = 0

                        if und_inicial == 3:
                            resul = valor
                        elif und_inicial == 1:
                            result = valor / 3600
                        elif und_inicial == 2:
                            resul = valor / 60
                        else:
                            resul = valor * 24

                        print(f'El resultado es: {resul}h')
                        break

                    # convertir a dias
                    case 3:
                        resul = 0

                        if und_inicial == 4:
                            resul = valor
                        elif und_inicial == 1:
                            result = valor / 86400
                        elif und_inicial == 2:
                            resul = valor / 1440
                        else:
                            resul = valor / 24

                        print(f'El resultado es: {result} días')
                        break
            else:
                print('ERROR > La opción ingresada no es válida')
                break
                    
