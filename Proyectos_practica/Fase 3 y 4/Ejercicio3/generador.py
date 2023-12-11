
import random
import math


def leer_numero(ini, fin, mensaje):

    while True:
        try:
            valor = int(input(mensaje))
        except:
            print('Error, numerr no válido')
        else:
            if valor >= 0 and valor <= fin:
                break

    return valor


def generador():
    numeros = leer_numero(1,20,'Cuántos números quieres generar? [1-20]')
    modo = leer_numero(1,3,'¿Cómo quieres redondear los números?\n[1] Al alza\n[2] A la baja\n[3] Normal')


    lista = []

    for i in range(numeros):
        numero = random.uniform(1,101)

        if modo == 1:
            print(f'{numero} => {math.ceil(numero)}')
            numero = math.ceil(numero)

        elif modo == 2:
            print(f'{numero} => {math.floor(numero)}')
            numero = math.floor(numero)

        elif modo == 3:
            print(f'{numero} => {round(numero)}')
            numero = round(numero)

        lista.append(numero)
    return lista


generador()