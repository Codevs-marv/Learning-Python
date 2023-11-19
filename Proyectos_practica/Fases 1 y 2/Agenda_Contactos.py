# E J E R C I C I O
#  Crea una aplicación de agenda de contactos que permita al usuario agregar, editar, eliminar y ver contactos. Utiliza diccionarios para almacenar la información de contacto.

agenda = []

while True:  # Bucle principal
    print('¿Qué quieres hacer en tu agenda de contactos?')
    print("""
        [1] Agregar contacto
        [2] Editar contacto
        [3] Buscar contacto
        [4] Eliminar contacto
        [5] Salir
    """)

    accion = int(input('Digite el número de la opción: '))

    if accion == 5:  # Opción para salir
        break


    match accion:
        # Agregar contacto

        case 1:
            contact = {
                'Nombre': input('Ingrese nombre: '),
                'Celular': input('Ingrese N° celular: '),
                'Categoria': input('Indique tipo de relación con el contacto (amigo,primo,mamá,hermano,etc): ')
            }
            agenda.append(contact)
            print('Contacto agregado con éxito')

    
        # Editar contacto
        case 2:
            while True:
                editar = input('Ingrese el nombre del contacto que quiere editar: ')
                encontrado = False
                for contacto in agenda:
                    if contacto["Nombre"] == editar:
                        encontrado = True
                        break
                if not encontrado:
                    print('Ese contacto no existe')
                else:
                    break

            print('¿Qué quiere editar?')
            print("""
                [1] Nombre
                [2] Celular
                [3] Categoría
            """)
            opcion = int(input("Digite el numero de la opcion: "))

            # Cambiar nombre
            if opcion == 1:
                nuevo_nombre = input('Ingrese el nuevo nombre: ')

                for contacto in agenda:
                    contacto["Nombre"] = nuevo_nombre
                    print('El nombre del contacto ha sido actualizado')
                    break

            # Cambiar celular            
            elif opcion == 2:
                nuevo_numero = int(input('Ingrese el nuevo número de celular: '))

                for contacto in agenda:
                    contacto['Celular'] = nuevo_numero
                    print('Número de celular actualizado')
                    break

            # Cambiar categoría            
            elif opcion == 3:
                nueva_categoria = input('Ingrese la nueva categoría del contacto: ')

                for contacto in agenda:
                    contacto['Categoria'] = nueva_categoria
                    print('Nueva categoría actualizada')
                    break


        # Buscar contacto                
        case 3:
            print('¿Cómo quiere buscar el contacto?')
            print("""
                [1] Por nombre
                [2] Por celular
            """)
            option = int(input('Digite el numero de la opción: '))
            
            # Buscar por nombre
            if option == 1:
                buscarnombre = input('Ingrese el nombre del contacto que desea buscar: ')

                encontrado = False
                for contacto in agenda:
                    if contacto['Nombre'] == buscarnombre:
                        print(contacto)
                        encontrado = True
                        break

                if not encontrado:
                    print('El nombre no se encontró, el contacto no existe')

            # Buscar por N° celular        
            else:
                buscarcelular = int(input('Ingrese el número de celular que desea buscar'))

                encontrado = False
                for contacto in agenda:
                    if contacto['Celular'] == buscarcelular:
                        print(contacto)
                        encontrado = True
                        break

                if not encontrado:
                    print('El número no está registrado, el contacto no existe')
 

        # Eliminar contacto
        case 4:
            eliminar = input('Digite el nombre del contacto que desea eliminar: ')

            for contacto in agenda:
                if contacto['Nombre'] == eliminar:
                    print('¿Estás seguro de eliminar el contacto?')
                    respuesta = input('Escriba "si" o "no": ')

                    if respuesta == "si":
                        agenda.remove(contacto)
                        print('>Contacto eliminado<')
                        break
                    else:
                        print('OK')
                        break
                else:
                    print('El contacto no está registrado')
                    break