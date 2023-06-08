from claseTaller import TallerCapacitacion
import numpy as np
import csv 
class arregloTaller:
    __dimension = 0
    __posicion = 0
    

    def __init__(self):
        archivo = open('talleres.csv')
        reader = csv.reader(archivo, delimiter=';')
        self.__dimension = int(next(reader)[0])
        self.__arregloTalleres = np.empty(self.__dimension, dtype=TallerCapacitacion)
        archivo.close()

    def agregaTaller(self, unTaller):
        self.__arregloTalleres[self.__posicion]=unTaller
        self.__posicion += 1 

    def carga(self):
        archivo = open('talleres.csv',encoding='utf-8')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            self.agregaTaller(TallerCapacitacion(fila[0],fila[1],fila[2],fila[3]))

    def mostrarTaller(self):
        i = 0
        for i in range(len(self.__arregloTalleres)):
           print("Id: ", self.__arregloTalleres[i].getId()," - ", self.__arregloTalleres[i].getNom())
            
    def TallerPorIndice(self,indice):
        return self.__arregloTalleres[indice-1]
                