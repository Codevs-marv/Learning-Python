                                                # MODULO DE FUNCIONES AUXILIARES #

import re
import os
import platform


def limpiar_pantalla():
    os.system('cls') if platform.system() == 'Windows' else os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None

    while True:
        texto = input('> ')

        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        

def cc_valido(cc, lista):
    if not re.match('[0-9]{2}[A-Z]$', cc):
        print('CC incorrecto, debe cumplir el formato')
        return False
    for cliente in lista:
        if cliente.cc == cc:
            print('CC utilizado por otro cliente')
            return False
    return True
    