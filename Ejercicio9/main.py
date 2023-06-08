import unittest
from test import TestVehiculos
from claseListaVehiculo import ListaVehiculos
from claseVehiculo import Vehiculo

def main():
    lista_vehiculos = ListaVehiculos()
    lista_vehiculos.cargar_desde_archivo("vehiculos.json")

    while True:
        print("Menú de opciones:")
        print("1. Insertar un vehículo en la colección en una posición determinada")
        print("2. Agregar un vehículo a la colección")
        print("3. Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición ")
        print("4. Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
        print("5. Mostrar todos los datos, incluido el importe de venta, del vehículo más económico. ")
        print("6. Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta")
        print("7. Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
        print("8. Salir")

        opcion = int(input("Ingrese el número de la opción que desea realizar: "))

        if opcion == 1:
            # Insertar un vehículo
            modelo = input("Ingrese el modelo del vehículo: ")
            puertas = int(input("Ingrese la cantidad de puertas: "))
            color = input("Ingrese el color del vehículo: ")
            precio_base = float(input("Ingrese el precio base del vehículo: "))
            vehiculo = Vehiculo(modelo, puertas, color, precio_base)
            posicion = int(input("Ingrese la posición donde desea insertar el vehículo: "))
            usado = input("¿El vehículo es usado? (S/N): ")
            if usado.upper() == "S":
                patente = input("Ingrese la patente del vehículo: ")
                marca = input("Ingrese la marca del vehículo: ")
                anio = int(input("Ingrese el año del vehículo: "))
                kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
                vehiculo.set_usado(patente, marca, anio, kilometraje)
            lista_vehiculos.insertar(vehiculo, posicion)
        elif opcion == 2:
            # Agregar un vehículo
            modelo = input("Ingrese el modelo del vehículo: ")
            puertas = int(input("Ingrese la cantidad de puertas: "))
            color = input("Ingrese el color del vehículo: ")
            precio_base = float(input("Ingrese el precio base del vehículo: "))
            vehiculo = Vehiculo(modelo, puertas, color, precio_base)
            lista_vehiculos.agregar(vehiculo)
        elif opcion == 3:
            # Mostrar información de un vehículo por posición
            posicion = int(input("Ingrese la posición del vehículo que desea ver: "))
            print(lista_vehiculos.mostrar_informacion(posicion))
        elif opcion == 4:
            # Modificar precio base de un vehículo por patente y mostrar precio de venta
            patente = input("Ingrese la patente del vehículo para modificar el precio base: ")
            vehiculo = lista_vehiculos.buscar_por_patente(patente)
            if vehiculo:
                nuevo_precio_base = float(input("Ingrese el nuevo precio base: "))
                vehiculo.precio_base_venta = nuevo_precio_base
                print(f"El nuevo precio de venta es: {vehiculo.calcular_importe_venta_usado()}")
            else:
                print("No se encontró un vehículo con esa patente.")
        elif opcion == 5:
            # Mostrar vehículo más económico
            vehiculo_economico = lista_vehiculos.mostrar_vehiculo_economico()
            print(f"El vehículo más económico es: {vehiculo_economico}")
        elif opcion == 6:
            # Mostrar todos los vehículos
            lista_vehiculos.mostrar_datos()
        elif opcion == 7:
            # Guardar vehículos en el archivo
            nombre_archivo = input("Ingrese el nombre del archivo donde desea guardar los vehículos: ")
            lista_vehiculos.cargar_desde_archivo(nombre_archivo)
        elif opcion == 8:
            # Salir
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVehiculos)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    main()
    run_tests()