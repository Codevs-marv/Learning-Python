import copy
import helpers
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

    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('19RV', 'Marco', 'Rodriguez')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.cc, '19RV')
        self.assertEqual(nuevo_cliente.nombre, 'Marco')
        self.assertEqual(nuevo_cliente.apellido, 'Rodriguez')

    def test_modificar_cliente(self):
        cliente_modificar = copy.copy(db.Clientes.buscar('12A'))
        cliente_modificado = db.Clientes.modificar('12A', 'Mariana', 'Perez')
        self.assertEqual(cliente_modificar.nombre, 'Martha')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar('13B')
        cliente_rebuscado = db.Clientes.buscar('13B')
        self.assertEqual(cliente_borrado.cc, '13B')
        self.assertIsNone(cliente_rebuscado)

    def test_cc_valido(self):
        self.assertTrue(helpers.cc_valido('00A', db.Clientes.lista))
        self.assertFalse(helpers.cc_valido('234234n', db.Clientes.lista))
        self.assertFalse(helpers.cc_valido('F35', db.Clientes.lista))
        self.assertFalse(helpers.cc_valido('14C', db.Clientes.lista))
