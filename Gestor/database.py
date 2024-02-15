import csv


class Cliente:
    def __init__(self, cc, nombre, apellido):
        self.cc = cc 
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'({self.cc}) {self.nombre} {self.apellido}'


class Clientes:

    lista = []
    with open('clientes.csv', newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for cc,nombre,apellido in reader:
            cliente = Cliente(cc, nombre, apellido)
            lista.append(cliente)


    @staticmethod
    def buscar(cc):
        for cliente in Clientes.lista:
            if cliente.cc == cc:
                return cliente
            
    @staticmethod
    def crear(cc, nombre, apellido):
        cliente = Cliente(cc, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente
    
    @staticmethod
    def modificar(cc, nombre, apellido):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.cc == cc:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(cc):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.cc == cc:
                cliente = Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente
            
    
    @staticmethod
    def guardar():
        with open('clientes.csv', 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.cc, cliente.nombre, cliente.apellido))

