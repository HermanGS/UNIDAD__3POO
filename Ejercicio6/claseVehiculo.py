import json
import datetime

class Vehiculo:
    def __init__(self, modelo, puertas, color, precio_base, usado=False, marca=None, patente=None, año=0, kilometraje=0, version=None, gastos_patentamiento=0):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio_base = precio_base
        self.__usado = usado
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje
        self.__version = version
        self.__gastos_patentamiento = gastos_patentamiento

    def __str__(self):
        return f"Modelo: {self.__modelo}, Puertas: {self.__puertas}, Color: {self.__color}, Importe de venta: {self.get_importe_venta()}"

    def get_modelo(self):
        return self.__modelo

    def get_puertas(self):
        return self.__puertas

    def get_color(self):
        return self.__color

    def get_precio_base(self):
        return self.__precio_base

    def set_precio_base(self, precio_base):
        self.__precio_base = precio_base

    def get_usado(self):
        return self.__usado

    def get_marca(self):
        return self.__marca

    def get_patente(self):
        return self.__patente

    def get_año(self):
        return self.__año

    def get_kilometraje(self):
        return self.__kilometraje

    def get_version(self):
        return self.__version
    
    def set_usado(self, patente, marca, anio, kilometraje):
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.kilometraje = kilometraje

    def calcular_importe_venta_usado(self):
        precio_venta = self.precio_base_venta
        if self.anio:
            precio_venta -= (2023 - self.anio) * 1000  # Restar 1000 por cada año de antigüedad
        if self.kilometraje:
            precio_venta -= self.kilometraje * 0.1  # Restar 0.1 por cada kilómetro recorrido
        return precio_venta

    def get_importe_venta(self):
        if self.__usado:
            return self.__precio_base * (1 - 0.01 * (datetime.datetime.now().year - self.__año)) - self.__precio_base * 0.02 * (self.__kilometraje - 100000) if self.__kilometraje > 100000 else self.__precio_base * (1 - 0.01 * (datetime.datetime.now().year - self.__año))
        else:
            return self.__precio_base + self.__precio_base * 0.10 + self.__precio_base * 0.02 if self.__version == "full" else self.__precio_base + self.__precio_base * 0.10