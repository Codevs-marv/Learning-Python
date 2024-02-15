import os
import helpers
import database as db


def iniciar():
    while True:
        helpers.limpiar_pantalla() # Aux Function

        print('_________________________')
        print("   Bienvenido al Gestor  ")
        print('-------------------------')
        print('[1] Listar los clientes')
        print('[2] Buscar un cliente')
        print('[3] Añadir un cliente')
        print('[4] Modificar un cliente')
        print('[5] Borrar un cliente')
        print('[6] Cerrar el gestor')
        print('_________________________\n')

        opcion = input('> ')
        helpers.limpiar_pantalla() # Aux Function
        
        if opcion == '1':
            print('Listando los clientes...\n')
            for cliente in db.Clientes.lista:
                print(cliente)

        elif opcion == '2':
            print('Buscando un cliente...\n')
            cc = helpers.leer_texto(3, 3, 'CC (2 nums y 1 char)').upper()
            cliente = db.Clientes.buscar(cc)
            print(cliente) if cliente else print('Cliente no encontrado.')

        elif opcion == '3':
            print('Añadiendo un cliente...\n')

            cc = None
            while True:
                cc = helpers.leer_texto(3, 3, 'CC (2 nums y 1 letra)').upper()
                if helpers.cc_valido(cc, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, 'Nombre (De 2 a 30 chars)').capitalize()
            apellido = helpers.leer_texto(2, 30, 'Apellido (De 2 a 30 chars)').capitalize()
            db.Clientes.crear(cc, nombre, apellido)
            print('Cliente añadido correctamente.')

        elif opcion == '4':
            print('Modificando cliente...\n')
            cc = helpers.leer_texto(3, 3, 'CC (2 nums y 1 letra)').upper()
            cliente = db.Clientes.buscar(cc)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f'Nombre (De 2 a 30 chars) [{cliente.nombre}]').capitalize()
                apellido = helpers.leer_texto(2, 30, f'Apellido (De 2 a 30 chars) [{cliente.apellido}]').capitalize()
                db.Clientes.modificar(cliente.cc, nombre, apellido)
                print('Cliente modificado correctamente.')
            else:
                print('Clienten no encontrado.')

        elif opcion == '5':
            print('Borrando cliente...\n')
            cc = helpers.leer_texto(3, 3, 'CC (2 nums y 1 letra)').upper()
            print('Cliente borrado correctamente.') if db.Clientes.borrar(cc) else print('Cliente no encontrado.')
            
        elif opcion == '6':
            print('Saliendo...\n')
            break
    
        input('\nPresiona ENTER para continuar...')