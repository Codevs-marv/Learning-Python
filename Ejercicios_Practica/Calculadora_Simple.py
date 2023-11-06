# E J E R C I C I O
# Crear una calculadora simple que le solicite al usuario dos números y la operación que desea realizar entre dichos números.

from __future__ import annotations


print('C A L C U L A D O R A')
print('A continuación digita 2 números enteros cualesquiera y la operación que desea realizar')

n1 = int(input('Ingrese el primer número: '))
n2 = int(input('Ingrese el segundo número: '))

while True:
    print('¿Qué operación quiere realizar?')
    print(""" 
    [1] Suma
    [2] Resta
    [3] Multiplicación
    [4] División
    [5] Exponenciación
    [6] Mayor o menor que
    [7] Radicación
    """)
    operacion = int(input())

    match operacion:
        case 1:
            print(f'La suma de {n1} y {n2} es: {n1+n2}')
            break
        case 2:
            print(f'La resta de {n1} y {n2} en ese orden, es: {n1-n2}')
            break
        case 3:
            print(f'El producto de {n1} y {n2} es: {n1*n2}')
            break
        case 4:
            print(f'El cociente de {n1} entre {n2} es: {n1/n2}')
            break
        case 5:
            print(f'El resultado de {n1} elevado a la {n2} es: {n1**n2}')
            break
        case 6:
            if n1 > n2:
                print(f'{n1} es mayor que {n2}')
                break
            elif n1 < n2:
                print(f'{n2} es mayor que {n1}')
                break
            else:
                print('Los números son iguales')
                break
        case 7:
            print('¿Cuál número será el índice de la raíz?')
            indice = int(input('Escribalo: '))

            if indice != n1 and indice != n2:
                print('El índice debe ser uno de los números ya ingresados')
                break
            else:
                if indice == n1:
                    print(f'El resultado de la raíz {n1} de {n2} es: {n2 ** (1/n1)}')
                    break
                else:
                    print(f'El resultado de la raiz {n2} de {n1} es: {n1 ** (1/n2)}')
                    break
        