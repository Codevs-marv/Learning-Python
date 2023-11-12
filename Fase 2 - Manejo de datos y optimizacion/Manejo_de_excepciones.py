n = float(input('Ingrese un número: '))
m = 4
print(f'{n}/{m} = {n/m}') # si el usuario ingresa algo distinto a un numero genera un error


#>> E X C E P C I O N E S > Anticipar errores
while True:
    try: # captura el error
        n = float(input('Ingrese un número: '))
        m = 4
        print(f'{n}/{m} = {n/m}')   
        break
    except: # la excepción
        print('Ha ocurrido un error, parece que no introduciste un número')

    finally:  # ocurre indiferentemente de si hay excepciones o no
        print('Fin de la iteración')



#  >>> M U L T I P L E S   E X C E P C I O N E S  <<< #

try:
    n = float(input('Introduce un número: '))
    5/n
except TypeError: # excepción específica
    print('No se puede dividir por una cadena')

except ValueError: # excepción específica
    print('Debes introducir una cadena que sea un número')

except ZeroDivisionError: # excepción específica
    print('No se puede dividir entre cero, prueba otro número')

except Exception as e:
    print(type.__name__)  # muestra el tipo de error --> TypeError

