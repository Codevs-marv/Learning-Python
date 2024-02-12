class Cliente:
    def __init__(self, cc, nombre, apellido):
        self.cc = cc 
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'({self.cc}) {self.nombre} {self.apellido}'


class Clientes:

    lista = []

    @staticmethod
    def buscar(cc):
        for cliente in Clientes.lista:
            if cliente.cc == cc:
                return cliente
            
    @staticmethod
    def crear(cc, nombre, apellido):
        cliente = Cliente(cc, nombre, apellido)
        Clientes.lista.append(cliente)
        return cliente
    
    @staticmethod
    def modificar(cc, nombre, apellido):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.cc == cc:
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido = apellido
                return Clientes.lista[indice]
            
    @staticmethod
    def borrar(cc):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.cc == cc:
                return Clientes.lista.pop(indice)