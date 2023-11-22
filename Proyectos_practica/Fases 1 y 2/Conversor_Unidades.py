def convertir_longitud(valor, und_inicial, convertir_a):
    # Diccionario con factores de conversión a metros
    factores_a_metros = {
        1: 0.001,  # Milimetros a Metros
        2: 0.01,   # Centimetros a Metros
        3: 0.0254, # Pulgadas a Metros
        4: 0.3048, # Pies a Metros
        5: 1,      # Metros a Metros
        6: 1000,   # Kilometros a Metros
        7: 1609.34 # Millas a Metros
    }

    # Convertir a metros primero
    valor_en_metros = valor * factores_a_metros[und_inicial]

    # Convertir de metros a la unidad deseada
    valor_convertido = valor_en_metros / factores_a_metros[convertir_a]
    return valor_convertido

def convertir_temperatura(valor, und_inicial, convertir_a):
    if und_inicial == convertir_a:
        return valor
    
    # Celsius
    if und_inicial == 1:  
        if convertir_a == 2:  # a Fahrenheit
            return (valor * 9/5) + 32
        elif convertir_a == 3:  # a Kelvin
            return valor + 273.15
    
    # Fahrenheit
    elif und_inicial == 2:  
        if convertir_a == 1:  # a Celsius
            return (valor - 32) * 5/9
        elif convertir_a == 3:  # a Kelvin
            return ((valor - 32) * 5/9) + 273.15

    # Kelvin
    elif und_inicial == 3:  
        if convertir_a == 1:  # a Celsius
            return valor - 273.15
        elif convertir_a == 2:  # a Fahrenheit
            return ((valor - 273.15) * 9/5) + 32


def convertir_tiempo(valor, und_inicial, convertir_a):
    # Diccionario con factores de conversión a segundos
    factores_a_segundos = {
        1: 1,        # Segundos a Segundos
        2: 60,       # Minutos a Segundos
        3: 3600,     # Horas a Segundos
        4: 86400     # Dias a Segundos
    }

    # Convertir a segundos primero
    valor_en_segundos = valor * factores_a_segundos[und_inicial]

    # Convertir de segundos a la unidad deseada
    valor_convertido = valor_en_segundos / factores_a_segundos[convertir_a]
    return valor_convertido

print('C O N V E R S O R   DE   U N I D A D E S\n')

while True:
    print('¿Con qué unidades de medida quiere trabajar?')
    print("""
        [1] Longitud
        [2] Temperatura
        [3] Tiempo
    """)
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print('Por favor, ingrese un número válido')
        continue

    print('Ingrese una cantidad: ')
    try:
        valor = float(input("Cantidad: "))  # --> valor a convertir
    except ValueError:
        print('Por favor, ingrese un número válido')
        continue

    # Unidad de medida inicial
    print('¿En qué unidades se encuentra el número ingresado?')
    unidades = {
        1: ["Milimetros", "Centimetros", "Pulgadas", "Pies", "Metros", "Kilómetros", "Millas"],
        2: ["Grados Celsius", "Grados Fahrenheit", "Grados Kelvin"],
        3: ["Segundos", "Minutos", "Horas", "Días"]
    }

    for i, unidad in enumerate(unidades[opcion], 1):
        print(f"[{i}] {unidad}")

    try:
        und_inicial = int(input("Unidad inicial: "))
    except ValueError:
        print('Por favor, ingrese un número válido')
        continue

    # Unidad de medida que se desea obtener
    print('Convertir a:')
    for i, unidad in enumerate(unidades[opcion], 1):
        print(f"[{i}] {unidad}")

    try:
        convertir_a = int(input("Convertir a: "))
    except ValueError:
        print('Por favor, ingrese un número válido')
        continue

    if opcion == 1:  # Longitud
        resultado = convertir_longitud(valor, und_inicial, convertir_a)
        print(f'El resultado es: {resultado} {unidades[opcion][convertir_a-1]}')
    elif opcion == 2:  # Temperatura
        resultado = convertir_temperatura(valor, und_inicial, convertir_a)
        print(f'El resultado es: {resultado} {unidades[opcion][convertir_a-1]}')
    elif opcion == 3:  # Tiempo
        resultado = convertir_tiempo(valor, und_inicial, convertir_a)
        print(f'El resultado es: {resultado} {unidades[opcion][convertir_a-1]}')
    else:
        print('ERROR > Opción ingresada no válida')
