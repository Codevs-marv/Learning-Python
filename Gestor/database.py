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
            