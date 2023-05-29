import csv
from Sabor import Sabor

class ManejaSabores: 
    
    def __init__(self):
        self.__ListaSabores = []

    def IngresoArchivo(self):
        nombrearchivo = 'Sabores.csv'
        archivo = open(nombrearchivo)
        reader = csv.reader(archivo,delimiter = ',')
        for fila in reader:
            id = int(fila[0])
            Nombre = str(fila[1])
            Ingredientes = str(fila[2])
            SaborTemp = Sabor(id,Nombre,Ingredientes)
            self.__ListaSabores.append(SaborTemp)
            print("Agregando Sabor -->  ",SaborTemp)
        print("\n Fin Ingreso del Archivo ...")
        archivo.close()

    def MostrarSaboresTodos(self):
        print("... Mostrando Sabores ...")
        for i in range(len(self.__ListaSabores)):
            print(self.__ListaSabores[i])

    