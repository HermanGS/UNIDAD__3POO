from Nodo import Nodo
from Profesor import Profesor

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


    def ImprimirElementoCabeza(self):
        print(self.__Comienzo.getDato())

    def agregarElemento(self,elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__Comienzo)
        self.__Comienzo = nodo
        self.__actual = nodo
        self.__tope = self.__tope + 1


    def append(self,elemento):
        nuevonodo = Nodo(elemento)

        aux = self.__Comienzo
        if self.__Comienzo == None:
            self.__Comienzo = nuevonodo
            self.__actual = self.__Comienzo
            self.__tope += 1
        
        else:
            while aux.getSiguiente()!=None:
                aux = aux.getSiguiente()
            aux.setSiguiente(nuevonodo)
            self.__tope += 1




    def AgregarAlFinal(self,elemento):
        print("Agregando al Final de la lista")
        nuevoNodo = Nodo(elemento)
        
        aux = self.__Comienzo

        if self.__Comienzo == None:
            self.__Comienzo = nuevoNodo
            self.__tope += 1

        else:
            while aux.getSiguiente():
                #print(aux.getDato())
                aux = aux.getSiguiente()
            print("AUX",aux.getDato())
            aux.setSiguiente(nuevoNodo)
            self.__tope = self.__tope + 1

            print("\n")


    def AgregarFinalTest(self):
        Profesor4 = Profesor(42711885,"Moreno","Camila")
        nuevoNodo = Nodo(Profesor4)
        aux = self.__Comienzo

        if self.__Comienzo == None:
            self.__Comienzo = nuevoNodo
            self.__tope += 1
        else:
            while aux.getSiguiente():
                #print(aux.getDato())
                aux = aux.getSiguiente()
            print("AUX",aux.getDato())
            aux.setSiguiente(nuevoNodo)
            self.__tope = self.__tope + 1
            print("fin while")
            print("\n")


    #interfaces
    def insertarelemento(self, pos, objeto):
        counter = 1
        cabeza = self.__Comienzo
        if self.__Comienzo is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__Comienzo)
            self.__Comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        while counter < pos - 1 and cabeza is not None:
            counter += 1
            cabeza = cabeza.getSiguiente()
        if pos == 1:
            newNode = Nodo(objeto)
            newNode.setSiguiente(cabeza)
            self.__Comienzo = newNode
            self.__actual = newNode
        else:
            newNode = Nodo(objeto)
            newNode.setSiguiente(cabeza.getSiguiente())
            cabeza.setSiguiente(newNode)
        self.__tope+=1



    def insertarelemento2(self,pos,objeto):
        contador = 0
        aux = self.__Comienzo

        if self.__Comienzo == None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__Comienzo)
            self.__Comienzo = Nodo
            self.__actual = nodo
            self.__tope += 1

        while contador < pos - 1 and aux != None:
            contador += 1
            aux = aux.getSiguiente()
        
        if pos == 1:
            nuevonodo = Nodo(objeto)
            nuevonodo.setSiguiente(aux)
            self.__Comienzo = nuevonodo
            self.__actual = nuevonodo
            self.__tope += 1
        else:
            nuevonodo = Nodo(objeto)
            nuevonodo.setSiguiente(aux.getSiguiente())
            aux.setSiguiente(nuevonodo)
            self.__tope+=1


    def recorrerLista(self):
        aux = self.__Comienzo

        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
    
        print("\n")


    def recorrerLista2(self):
        aux = self.__Comienzo

        while aux.getSiguiente():
            print(aux.getDato())
            aux = aux.getSiguiente()
        print("fin while")
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

        



    def retornaTOPE(self):
        return self.__tope

    def retornaLongitud(self):
        aux = self.__Comienzo
        longitud = 0
        while aux != None:
            longitud = longitud + 1
            aux = aux.getSiguiente()
        return longitud




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



    def insertar(self,pos,elemento):                 # He logrado la Inserción  opcion 1
        contador = 1
        aux = self.__Comienzo
        bandera = False

        if self.__Comienzo == None:
            self.agregarElemento(elemento)

        if pos == 1:
            self.agregarElemento(elemento)
        else :
            ant = aux
            aux = aux.getSiguiente()
            contador += 1
            print("antes de entrar")
            while bandera == False and aux != None:
                if contador == pos:
                    bandera = True
                    print("encontro")
                else:
                    ant = aux
                    aux = aux.getSiguiente()
                    contador += 1
                    print("recorriendo contando : ",contador)
            
            if bandera:
                nodo = Nodo(elemento)
                nodo.setSiguiente(aux)
                ant.setSiguiente(nodo)
                print("if si")
            


    def insertarelementoHerman(self,pos,objeto):    # Insercion del ari  opcion 2
        contador = 0
        aux = self.__Comienzo

        if self.__Comienzo == None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__Comienzo)
            self.__Comienzo = Nodo
            self.__actual = nodo
            self.__tope += 1

        while contador < pos - 1 and aux != None:
            contador += 1
            aux = aux.getSiguiente()
        
        if pos == 1:
            nuevonodo = Nodo(objeto)
            nuevonodo.setSiguiente(aux)
            self.__Comienzo = nuevonodo
            self.__actual = nuevonodo
            self.__tope += 1
        else:
            nuevonodo = Nodo(objeto)
            nuevonodo.setSiguiente(aux.getSiguiente)
            aux.setSiguiente(nuevonodo)