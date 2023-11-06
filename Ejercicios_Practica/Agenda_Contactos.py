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
    case 1:
        contact = {}
        contact[f'Amigo{cantidad}'] = {'Nombre':input('Ingrese nombre: '),'Celular':input('Ingrese N° celular: '),'Categoría':input('Indique tipo de relación con el contacto (amigo,primo,mamá,hermano,etc): ')}
        agenda.append(contact)
        cantidad += 1
    
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

        if opcion == 1:
            nuevo_nombre = input('Ingrese el nuevo nombre: ')
            for contacto in agenda:
                if contacto["Nombre"] == editar:
                    contacto["Nombre"] = nuevo_nombre
                    print('El nombre del contacto ha sido actualizado')
                    break

        elif opcion == 2:
            for contacto in agenda:
                contacto