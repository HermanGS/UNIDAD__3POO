from Nodo import Nodo

class ListaEnlazada:
    __Comienzo : Nodo

    def __init__(self):
        self.__Comienzo = None

    def agregarElemento(self,elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__Comienzo)
        self.__Comienzo = nodo








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
            self.__Comienzo = aux.getSiguiente()
            del aux
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
                ant.getSiguiente(aux.getSiguiente())
                del aux
            else:
                print("No se encontro el dni buscado ")



