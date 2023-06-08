from Nodo import Nodo

class ListaEnlazada2:
    __Comienzo : Nodo
    __actual : Nodo
    __indice : int
    __tope : int


    def __init__(self):
        self.__Comienzo = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__Comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice  = self.__indice + 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato


    def __next__2(self):
        if self.__indice == self.__tope:
            self.__actual = self.__Comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice = self.__indice + 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato




    def agregarElemento(self,elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__Comienzo)
        self.__Comienzo = nodo
        self.__actual = nodo
        self.__tope = self.__tope + 1








    def recorrerLista(self):
        aux = self.__Comienzo

        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    
        print("\n")


    def busquedaBanderaDNI(self,dni):
        aux = self.__Comienzo
        bandera = False
        elemento = None
        print("gola putos")
        while aux != None and bandera == False:
            if aux.getDato().getDni() == dni:
                bandera = True
                elemento = aux.getDato()

        

    




    def eliminarProfesorPorDni(self,dni):
        aux = self.__Comienzo
        encontrado = False
        if aux.getDato().getDni() == dni:  #Primera posición
            encontrado = True
            print("Encontrado : ",str(aux.getDato()))   # lo que se hace cdo se encuentra
            self.__Comienzo = aux.getSiguiente()

            del aux
        
        else:  # No está en la primera posición
            ant = aux
            aux = aux.getSiguiente()
            while encontrado == False and aux != None:
                if aux.getDato().getDni() == dni:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if encontrado:
                pass
                


            
    def eliminarProfesorPorDni2(self,dni):
        aux = self.__Comienzo
        encontrado = False
        if aux.getDato().getDni() == dni:
            encontrado = True
            print("Profe comienzo antes",self.__Comienzo.getDato())
            self.__Comienzo = aux.getSiguiente()
            print("Profe comienzo dps",self.__Comienzo.getDato())
            print("Elimino profesor que SI es el primero ")
            del aux
            self.__tope = self.__tope - 1
        else:
            ant = aux
            aux = aux.getSiguiente()
            while encontrado == False and aux != None:
                if aux.getDato().getDni() == dni:
                    encontrado = True
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            if encontrado:
                ant.setSiguiente(aux.getSiguiente())
                print("Elimino profesor que NO es el primero ")
                del aux
                self.__tope = self.__tope - 1
            else:
                print("No se encontro el dni buscado ")



