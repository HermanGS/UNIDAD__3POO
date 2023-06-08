import numpy as np
from claseEmpleado import Empleado
from claseEmpExterno import EmpleadoExterno
from claseEmpPlanta import EmpleadoPlanta
from claseEmpContratado import EmpleadoContratado
import csv

class manejaEmpleados:
    __dimension = 0
    __posicion = 0
    __arregloEmpleados = None
    
    def __init__(self,dimension):
        self.__dimension = dimension
        self.__arregloEmpleados = np.empty(self.__dimension, dtype=Empleado)
        
    def agregaEmpleado(self, unEmpleado):
        self.__arregloEmpleados[self.__posicion]= unEmpleado
        self.__posicion += 1
        
    def carga(self):
        archivo1 = open('planta.csv',encoding='utf-8')
        reader = csv.reader(archivo1, delimiter=';')
        for fila in reader:
            self.agregaEmpleado(EmpleadoPlanta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
        archivo1.close()
        archivo2 = open('externo.csv',encoding='utf-8')
        reader = csv.reader(archivo2, delimiter=';')
        for fila in reader:
            self.agregaEmpleado(EmpleadoExterno(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9]))
        archivo2.close()
        archivo3 = open('contratado.csv',encoding='utf-8')
        reader = csv.reader(archivo3, delimiter=';')
        for fila in reader:
            self.agregaEmpleado(EmpleadoContratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7]))
        archivo3.close()
        
    def buscarDni(self, dni, horas):
        i = 0
        band = False
        while i < len(self.__arregloEmpleados) and band == False:
            if dni == self.__arregloEmpleados[i].getDni():
                band = True
                hs = self.__arregloEmpleados[i].actualizarHoras(horas)
                print("Cantidad de horas trabajadas: ", hs)
            i = i + 1
    
    def muestraMontoObra(self, tarea):
        i = 0
        band = False
        while (i<len(self.__arregloEmpleados) and band == False):
            if (type(self.__arregloEmpleados[i]) == EmpleadoExterno):
                if self.__arregloEmpleados[i].getTarea() == tarea:
                    band = True 
                    montoObra = self.__arregloEmpleados[i].getMontoObra()
                    print('Costo de la obra: {}'.format(montoObra))
            else:
                i = i + 1
                
    def mostrarSueldos (self):
        for empleado in self.__arregloEmpleados:
            print("Nombre: ", empleado.getNombre())
            print("Telefono: ", empleado.getTelefono()) 
            print("Sueldo: ", empleado.getSueldo())
            
            """if type(empleado)==EmpleadoContratado:
                print("Sueldo: ", empleado.getSueldoContratado())
            if type(empleado)==EmpleadoExterno:
                print("Sueldo: ", empleado.getSueldoExterno()) 
            if type(empleado)==EmpleadoPlanta:
                print("Sueldo: ", empleado.getSueldoPlanta())"""    
            
    def ayudaEconomica (self):
        for empleado in self.__arregloEmpleados:
            if empleado.getSueldo() < 2000:
                print("Nombre: {} Dni: {} Direccion: {} ".format(empleado.getNombre(), empleado.getDni(), empleado.getDirec()))
                      
                
              