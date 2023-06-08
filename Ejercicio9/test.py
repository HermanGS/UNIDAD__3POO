import unittest
from claseVehiculo import Vehiculo
from claseListaVehiculo import ListaVehiculos

class TestVehiculos(unittest.TestCase):
    def setUp(self):
        self.lista_vehiculos = ListaVehiculos()
        self.vehiculo1 = Vehiculo("Marca1", "Modelo1", 2000, 10000)
        self.vehiculo2 = Vehiculo("Marca2", "Modelo2", 3000, 15000)

    def test_agregar_vehiculo(self):
        self.lista_vehiculos.agregar(self.vehiculo1)
        self.assertEqual(self.lista_vehiculos.mostrar_informacion(0), self.vehiculo1)

    def test_insertar_vehiculo(self):
       self.lista_vehiculos.agregar(self.vehiculo1)
       self.lista_vehiculos.insertar(1, self.vehiculo2)
       self.assertEqual(self.lista_vehiculos.mostrar_informacion(1), self.vehiculo2)

    def test_obtener_vehiculo(self):
        self.lista_vehiculos.agregar(self.vehiculo1)
        vehiculo_obtenido = self.lista_vehiculos.mostrar_informacion(0)
        self.assertEqual(vehiculo_obtenido, self.vehiculo1)

    def test_modificar_precio_base(self):
        self.lista_vehiculos.agregar(self.vehiculo1)
        nuevo_precio = 12000
        self.vehiculo1.set_precio_base(nuevo_precio)
        self.assertEqual(self.vehiculo1.get_precio_base(), nuevo_precio)

if __name__ == '__main__':
    unittest.main()