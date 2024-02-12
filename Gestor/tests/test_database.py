import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('12A', 'Martha', 'Perez'),
            db.Cliente('13B', 'Manolo', 'Gonzales'),
            db.Cliente('14C', 'Cristian', 'Munoz'),
        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('12A')
        cliente_inexistente = db.Clientes.buscar('123Z')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)