# E J E R C I C I O
#  Crea una aplicación de agenda de contactos que permita al usuario agregar, editar, eliminar y ver contactos. Utiliza diccionarios para almacenar la información de contacto.

agenda = []

print('¿Qué quieres hacer en tu agenda de contactos?')
print("""
    [1] Agregar contacto
    [2] Editar contacto
    [3] Buscar contacto
    [4] Eliminar contacto
""")

accion = int(input('Digite el número de la opción: '))
cantidad = 0

match accion:
    # Agregar contacto
    case 1:
        contact = {}
        contact[f'Amigo{cantidad}'] = {'Nombre':input('Ingrese nombre: '),'Celular':input('Ingrese N° celular: '),'Categoría':input('Indique tipo de relación con el contacto (amigo,primo,mamá,hermano,etc): ')}
        agenda.append(contact)
        cantidad += 1
    
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
                if contacto["Nombre"] == editar:
                    contacto["Nombre"] = nuevo_nombre
                    print('El nombre del contacto ha sido actualizado')
                    break

        # Cambiar celular            
        elif opcion == 2:
            nuevo_numero = int(input('Ingrese el nuevo número de celular: '))

            for contacto in agenda:
                if contacto['Celular'] == editar:
                    contacto['Celular'] = nuevo_numero
                    print('Número de celular actualizado')
                    break

        # Cambiar categoria            
        elif opcion == 3:
            nueva_categoria = input('Ingrese la nueva categoría del contacto: ')

            for contacto in agenda:
                if contacto['Categoría'] == editar:
                    contacto['Categoría'] = nueva_categoria
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

            for contacto in agenda:
                if contacto['Nombre'] == buscarnombre:
                    print(contacto)
                    break
                else:
                    print('El nombre no se encontró, el contacto no existe')
                    break

        # Buscar por N° celular        
        else:
            buscarcelular = int(input('Ingres el numero de celular que desea buscar'))

            for contacto in agenda:
                if contacto['Celular'] == buscarcelular:
                    print(contacto)
                    break
                else:
                    print('El número no está registrado, el contacto no existe')
                    break