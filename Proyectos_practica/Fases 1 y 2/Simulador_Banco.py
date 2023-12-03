# E J E R C I C I O
'''Diseña un simulador de banco que permita a los usuarios crear cuentas, realizar depósitos y retiros, y consultar saldos. Implementa la lógica de manejo de cuentas y utiliza conceptos de manejo 
de archivos o bases de datos para almacenar la información de las cuentas.'''

import random
import datetime

print('B A N C O   S I M U L A D O R')

cuentas = []  # lista de cuentas creadas o existentes
fecha_hora_actual = datetime.datetime.now()

# Saber fecha y hora actuales para mostrar en los comprobantes de las transacciones
fecha = fecha_hora_actual.date()
hora = datetime.datetime.now().strftime("%H:%M")

while True:
    print('\n¿Qué quieres hacer?\n[1] Crear cuenta\n[2] Depositar\n[3] Retirar\n[4] Consultar saldo\n[5] Salir')

    try:
        opcion = int(input('Elige una opción: '))
    except ValueError:
        print('Opción no válida')
        continue

    if 1 <= opcion <= 5:

        if opcion == 5:
            print('Cerrando el simulador')
            break


        # CREAR CUENTA
        if opcion == 1:
            new_count = {}

            # escoger tipo de cuenta
            print('Escoge el tipo de cuenta que quieres crear:\n[1] Cuenta corriente\n[2] Ahorros ')
            try:
                tipo = int(input('Escoja una opción: '))
            except ValueError:
                print('Opción no válida')
                continue

            new_count['Tipo'] = 'corriente' if tipo == 1 else 'ahorros'

            # generar número de cuenta
            new_count['No_cuenta'] = random.randint(10 ** 11, (10 ** 12) - 1)

            # ingresar datos
            print('Ingresa nombre y apellido del titular: ')
            new_count['Titular'] = input()

            # Crear clave
            while True:
                print('Ingrese una clave de 4 dígitos para su cuenta')
                password = input()
                print('Confirme la clave')
                confirmed = input()

                if confirmed == password:
                    print('--> Se ha creado la clave con éxito')
                    new_count['Clave'] = password
                    break
                else:
                    print('Las claves no coinciden, inténtelo de nuevo')
                    continue

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
                    Saldo: ${new_count["Saldo"]}          
                ________________________________________
            """)


        # DEPÓSITO
        elif opcion == 2:
            print('Ingresa el número de cuenta al que depositarás:')
            try:
                cuenta = int(input())
            except ValueError:
                print('Debe ingresar un número de cuenta válido')
                continue

            for cuent in cuentas:
                if cuent['No_cuenta'] == cuenta:
                    while True:
                        print('Hará un depósito a una cuenta ya registrada')
                        print('Digite la cantidad que quiere depositar')
                        try:
                            depo = int(input())
                        except ValueError:
                            print('Cifra no válida, inténtelo de nuevo')
                            continue
                        cuent['Saldo'] += depo  # Agregar al saldo de la cuenta el depósito
                        print(f"""
                            -----------------------------------
                                COMPROBANTE DE TRANSACCIÓN
                              
                                valor depositado: ${depo}
                                destinatario: {cuenta}
                                    {fecha}, {hora}
                            -----------------------------------
                        """)
                        break
                    break
                    # No necesitas el bucle 'else' aquí

                else:
                    print('La cuenta ingresada no está registrada, inténtelo de nuevo')
                    break


        # RETIRAR
        elif opcion == 3:
            print('Recuerde que solo puede retirar dinero de cuentas ya registradas')
            print('Ingrese el número de cuenta: ')
            cuenta = int(input())

            exitoso = False

            for cuent in cuentas:
                if cuent['No_cuenta'] == cuenta:
                    print(f'El titular de la cuenta es', cuent['Titular'])
                    print('Digite la cantidad que quiere retirar: ')
                    cantidad = int(input())

                    if cuent['Saldo'] >= cantidad:
                        print('Digite la clave: ')
                        clave = input() 

                        if clave == cuent['Clave']:
                            print('Retirando dinero...')
                            cuent['Saldo'] -= cantidad
                            print(f"""
                                    ------------------------------
                                            -COMPROBANTE-
                                  
                                      Valor retirado = ${cantidad}                                  
                                          {fecha}, {hora}
                                    ------------------------------
                            """)
                            exitoso = True
                        else:
                            print('Clave incorrecta')
                            print('--Por su seguridad cancelaremos la transacción--')
                        
                        break  # Salir del bucle después de procesar la cuenta

                    else:
                        print('No tiene saldo suficiente, intente nuevamente con un valor menor')
                        break  # Salir del bucle después de procesar la cuenta

            if not exitoso:
                print('--TRANSACCIÓN CANCELADA--')


        # CONSULTAR SALDO
        elif opcion == 4:
            print('Recuerde que puede consultar saldos únicamente en cuentas ya registradas previamente')
            print('\nDigite el número de cuenta: ')
            cuenta = int(input())

            for cuent in cuentas:
                if cuent['No_cuenta'] == cuenta:
                    print(f'El titular de la cuenta es', cuent['Titular'])

                    while True:
                        print('\nIngrese la clave de su cuenta: ')
                        clave = input()

                        if clave == cuent['Clave']:
                            print('Clave correcta')
                            print(f"""
                                    ----------------------------------
                                              DATOS CONSULTA
                                  
                                         Titular: {cuent['Titular']}  
                                         Estado: Activa
                                         Saldo: ${cuent['Saldo']}

                                            {fecha}, {hora}
                                    ----------------------------------
                            """)
                            break
                        else:
                            print('Clave incorrecta, inténtelo de nuevo')
                            continue

    else:
        print('Opción no válida, inténtelo de nuevo')
