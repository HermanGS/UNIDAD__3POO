from claseVehiculo import Vehiculo
import json
import datetime

class ListaVehiculos:
    def __init__(self):
        self.vehiculos = []

    def __iter__(self):
        self.__indice = 0
        return self

    def __next__(self):
        if self.__indice < len(self.vehiculos):
            vehiculo = self.vehiculos[self.__indice]
            self.__indice += 1
            return vehiculo
        else:
            raise StopIteration

    def insertar(self, posicion, vehiculo):
        self.vehiculos.insert(posicion, vehiculo)

    def agregar(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrar_informacion(self, posicion):
        return self.vehiculos[posicion]

    def modificar_precio_base(self, patente, precio_base):
        for vehiculo in self.vehiculos:
            if vehiculo.get_patente() == patente:
                vehiculo.set_precio_base(precio_base)
                break

    def mostrar_vehiculo_economico(self):
        menor_importe = float('inf')
        vehiculo_economico = None
        for vehiculo in self.vehiculos:
            if vehiculo.get_importe_venta() < menor_importe:
                menor_importe = vehiculo.get_importe_venta()
                vehiculo_economico = vehiculo
        return vehiculo_economico

    def mostrar_datos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo)

    def buscar_por_patente(self, patente):
        for vehiculo in self.vehiculos:
            if vehiculo.patente == patente:
                return vehiculo
        return None

    def diccionarios_a_vehiculos(self, diccionarios_vehiculos):
        vehiculos = []
        for diccionario in diccionarios_vehiculos:
            vehiculo = Vehiculo(
                diccionario['modelo'],
                diccionario['puertas'],
                diccionario['color'],
                diccionario['precio_base_venta'],
                diccionario['patente'],
                diccionario['marca'],
                diccionario['anio'],
                diccionario['kilometraje'],
            )
            vehiculos.append(vehiculo)
        return vehiculos

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as f:
                contenido = f.read()
                if contenido:
                    diccionarios_vehiculos = json.loads(contenido)
                    self.vehiculos = self.diccionarios_a_vehiculos(diccionarios_vehiculos)
                else:
                    print(f"El archivo '{nombre_archivo}' está vacío. Se creará una nueva lista de vehículos.")
                    self.vehiculos = []
        except FileNotFoundError:
            print(f"El archivo '{nombre_archivo}' no existe. Se creará una nueva lista de vehículos.")
            self.vehiculos = []