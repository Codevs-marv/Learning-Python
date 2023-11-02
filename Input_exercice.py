# Realiza un programa con los siguientes requisitos:
# - Debes leer por teclado dos cadenas de caracteres, una llamada nombre y otra llamada apellido.
# - Debes leer por teclado un número entero llamado edad (recuerda que la variable debe ser de tipo entero).
# - Debes leer por teclado un número flotante llamado numero_magico.

# Finalmente debes crear una variable cadena_final con el siguiente formato:
    # NOMBRE APELLIDO: Tu número de la suerte es el EDAD*NUMERO_MAGICO

# Completa el ejercicio
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Digite su edad: "))
numero_magico = float(input("Ingrese un valor numerico cualquiera: "))

cadena_final = nombre + " " + apellido + ": " + "Tu numero de la suerte es el " + str(edad * numero_magico)
print(cadena_final)