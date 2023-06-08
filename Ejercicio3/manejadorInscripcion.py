from claseInscripcion import Inscripcion
import numpy as np

class manejaInscripcion:
    __dimension = 0
    __incremento = 5
    __cantidad = 0

    def __init__(self, dimension=5, incremento=5):
        self.__inscripciones = np.empty(dimension, dtype= Inscripcion)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
        
    def agregarInscripcion(self, unaInscripcion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad]=unaInscripcion
        self.__cantidad += 1
        

    """def MostrarInscripciones(self):
        for i in self.__inscripciones:
            if self.__inscripciones[i] != None:
                print(i)"""
                
    def MostrarInscripciones(self):            
        for inscripcion in self.__inscripciones:
            if inscripcion is not None:
                print(inscripcion)           

    def registrarInscripcion(self, Persona, taller):
        fecha = '5/6/23'
        taller.actualizarVacante()
        InscripcionTemporal = Inscripcion(fecha, Persona,taller)
        self.agregarInscripcion(InscripcionTemporal)
     
    def consultarInscripcion(self, dni):
        i = 0
        band = False
        while i < len(self.__inscripciones) and band == False:
            if self.__inscripciones[i].Persona().getDni() == dni:
                band = True
                print("Taller inscripto: ", self.__inscripciones[i].Taller().getNom(), "Monto a pagar: ", self.__inscripciones[i].Taller().getMonto())
            else:    
                i = i + 1