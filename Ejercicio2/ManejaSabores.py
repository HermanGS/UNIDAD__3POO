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
        if len(self.__ListaSabores) != 0:
            print("... Mostrando Sabores ...")
            for i in range(len(self.__ListaSabores)):
                print(self.__ListaSabores[i])
        else:
            print("No hay Sabores Registrados")
            print("\n")
        
    def MostrarSabores(self):
        for i in range(len(self.__ListaSabores)):
            print(self.__ListaSabores[i])


    def BuscarSaborID(self,id):
        i = 0
        while i < len(self.__ListaSabores) and self.__ListaSabores[i].retornaID() != id:
            i = i + 1
        if i <len(self.__ListaSabores):
            return self.__ListaSabores[i]
        #print("No se encontró el sabor Buscado por ID")

    def retornaCantidadSabores(self):
        return len(self.__ListaSabores)
    