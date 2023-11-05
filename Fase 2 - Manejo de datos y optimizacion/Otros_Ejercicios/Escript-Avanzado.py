'''Crea un script llamado descomposicion.py que realice las siguientes tareas:**
* Debe tomar 1 argumento que será un número entero positivo.
* En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.

** El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número:**

> 3647

** El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo: **

> 0007
  0040
  0600
  3000
'''




import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])

    if numero < 0 or numero > 9999:
        print('Error - Número es incorrecto')
    else:
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print('{:04d}'.format((int(cadena[longitud-1-i])) * (10 ** i)))
else:
    print('Error - Argumentos incorrectos')


# Truco:
# longitud-1-i   ---> recorrer al revés