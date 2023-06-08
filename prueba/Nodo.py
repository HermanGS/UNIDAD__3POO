from Profesor import Profesor  

class Nodo:
    __dato : Profesor
    __siguiente : object

    def __init__(self,Profesor) -> None:
        self.__dato  = Profesor
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente
    
    def getDato(self):
        return self.__dato
