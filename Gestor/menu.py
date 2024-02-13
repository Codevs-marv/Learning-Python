import os


def iniciar():
    while True:
        os.system('cls')

        print('_________________________')
        print("   Bienvenido al Gestor  ")
        print('-------------------------')
        print('[1] Listar los clientes')
        print('[2] Buscar un cliente')
        print('[3] Añadir un cliente')
        print('[4] Modificar un cliente')
        print('[5] Borrar un cliente')
        print('[6] Cerrar el gestor')

        opcion = input('> ')
        os.system('cls')
        
        if opcion == '1':
            print('Listando los clientes...\n')
            #
        elif opcion == '2':
            print('Buscando un cliente...\n')
            #
        elif opcion == '3':
            print('Añadiendo un cliente...\n')
            #
        elif opcion == '4':
            print('Modificando cliente...\n')
            #
        elif opcion == '5':
            print('Borrando cliente...\n')
            #
        elif opcion == '6':
            print('Saliendo...\n')
            break
    
        input('\nPresiona ENTER para continuar...')