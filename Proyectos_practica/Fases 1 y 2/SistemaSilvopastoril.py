def AreaValida(area):
    return 2 <= area <= 20

def area_conservacion(area):
    return area * 0.5

def Sistema(proposito, plantacion, metros2):
    #> Ganaderia
    if proposito == 'ganaderia':
        if plantacion == 'espiral':
            arboles, arbustos, animales = metros2/0.6, metros2/1.1, metros2/1.1
        elif plantacion == 'en filas':
            arboles, arbustos, animales = metros2/0.5, metros2/1.2, metros2/1
        elif plantacion == 'aleatoria':
            arboles, arbustos, animales = metros2/0.4, metros2/1, metros2/0.8
        else:
            print('Sin resultados debido a que no se conoce el tipo de plantación a utilizar')
            return None
    
    #> Agricola
    elif proposito == 'agricola':
        if plantacion == 'espiral':
            arboles, arbustos = metros2/0.8, metros2/1.4
        elif plantacion == 'en filas':
            arboles, arbustos = metros2/0.7, metros2/1.3
        elif plantacion == 'aleatoria':
            arboles, arbustos = metros2/0.5, metros2/1.2
        else:
            print('Sin resultados debido a que no se conoce el tipo de plantación a utilizar')
            return None
        
    # sin proósito
    else:
        print('Propósito no válido')
        return None

    resultados = {
        'arboles': arboles,
        'arbustos': arbustos,
        'animales': animales if proposito == 'ganaderia' else None
    }
    return resultados

# PROGRAMA PRINCIPAL
while True:
    try:
        print('Ingrese el área disponible en hectáreas: ')
        area = float(input())
    except ValueError:
        print('Error: Debes ingresar un número, inténtelo de nuevo')
        continue

    if not AreaValida(area):
        print('No se puede implementar un sistema con el área ingresada')
        break

    while True:
        try:
            print("""Seleccione el propósito del sistema:
            - Ganadería
            - Agrícola
                """)
            proposito = input().lower()

            print("""Seleccione el tipo de plantación (Escriba la opción):
            - Espiral
            - En filas
            - Aleatoria
                """)
            plantacion = input().lower()
        except Exception as e:
            print(f'Error: {e} > Debes ingresar una cadena de texto, inténtalo de nuevo')
            continue
        else:
            break

    metros_cuadrados = area * 10000 - area_conservacion(area) # --> area a trabajar
    resultados = Sistema(proposito, plantacion, metros_cuadrados)

    if resultados:
        print('RESULTADOS:\n')
        print(f'Se deben destinar {area_conservacion(area)} hectáreas a conservación')
        print(f'En el área a trabajar caben aproximadamente {resultados["arboles"]} arboles')
        print(f'En el área a trabajar caben aproximadamente {resultados["arbustos"]} arbustos')

        # Verificar si el propósito es ganadería antes de imprimir la cantidad de animales
        if proposito == 'ganaderia' and resultados["animales"] is not None:
            print(f'En el área a trabajar se pueden sostener aproximadamente {resultados["animales"]} animales')

    print("""\nDesea calcular la implementación de otro sistema?
        - Si
        - No
          """)
    opcion = input().lower()

    if opcion == 'no':
        print('OK, Cerrando el programa...\n Fin del programa')
        break
    else:
        continue
