# E J E R C I C I O
'''Diseña un simulador de banco que permita a los usuarios crear cuentas, realizar depósitos y retiros, y consultar saldos. Implementa la lógica de manejo de cuentas y utiliza conceptos de manejo 
de archivos o bases de datos para almacenar la información de las cuentas.'''

import random

print('B A N C O   S I M U L A D O R')

while True:
    print('\n¿Qué quieres hacer?\n[1] Crear cuenta\n[2] Depositar\n[3] Retirar\n[4] Consultar saldo')

    try:
        opcion = int(input('Elige una opción: '))
    except ValueError:
        print('Opción no válida')
        continue

    match opcion:
        
        # Crear cuenta
        case 1:
            cuentas = [] # lista de cuentas creadas o existentes
            new_count = {}

            # escoger tipo de cuenta
            print('Escoge el tipo de cuenta que quieres crear:\n[1] Cuenta corriente\n[2] Ahorros ')
            try:
                tipo = int(input('Escoja una opción'))
            except ValueError:
                print('Opción no válida')

            if tipo == 1:
                new_count['Tipo'] = 'corriente'
            else:
                new_count['Tipo'] = 'ahorros'
            
            # generar número de cuenta 
            new_count['No_cuenta'] = random.randint(10**11, (10**12)-1)

            # ingresar datos
            print('Ingresa nombre y apellido del titular: ')
            new_count['Titular'] = input()

            print('Desea añadir un saldo ahora?\n[1] Si\n[2] No')
            resp = int(input())

            # añadir saldo
            if resp == 1:
                saldo = int(input('Ingrese la cantidad que quiere ingresar a la cuenta: '))
                new_count['Saldo'] = saldo
                print(f'Se añadió a la cuenta un saldo de ${saldo}')
            else:
                new_count['Saldo'] = 0
                print('OK, su cuenta se creará sin saldo')

            cuentas.append(new_count)
            print('\nSu cuenta ha sido creada con éxito!')
            print(f"""
                Los datos de su cuenta son: 
                ________________________________________
                              
                    Titular: {new_count["Titular"]}      
                    Cuenta {new_count["Tipo"]}           
                    N° Cuenta: {new_count["No_cuenta"]}  
                    Saldo: {new_count["Saldo"]}          
                ________________________________________
            """)
            
            continue

        # Depósitos
        case 2:
            print('Ingrese el número de cuenta al que quiere depositar: ')
            cuenta = int(input())

            existe = False
            for dict in cuentas:
                if new_count['Cuenta'] == cuenta:
                    existe = True

            depositado = False
            while not depositado:    
                if existe:
                    try:
                        valor = int(input('Ingrese la cantidad que quiere depositar: '))
                        depositado = True
                    except ValueError:
                        print('ERROR: Debes ingresar una cantidad válida')
                        continue
                    
                    print('Procesando depósito...\nDepósito realizado con éxito!')
                    print(f'Se depositó en la cuenta {cuenta} la cantidad de {valor}')
