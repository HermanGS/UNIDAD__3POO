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
    
    def Sabores5MasPedidosOriginal(self,ManejadorHelados):
        listaContadores = []
        for i in range(len(self.__ListaSabores)):
            CantidadTotal = ManejadorHelados.ContarRepitenciaSabor(self.__ListaSabores[i])
            #listaContadores.append(CantidadTotal - CantidadTotal/2)
            listaContadores.append(CantidadTotal)


        listaDoble = list(zip(self.__ListaSabores,listaContadores))
        
        
        listaContadores.sort(reverse = True)
        
        if len(listaContadores) >= 5:
            print("Los 5 sabores más Pedidos : ")
            for i in range(5):
                print(self.__Contadores[i])
        else :
            print("Los 5 sabores más Pedidos : (No llegan a 5)") 
            for i in listaContadores:
                print(i)



        listaDoble.sort(key = lambda x : x[1] ,reverse = True)

        for i in range(len(listaDoble)):
            print(listaDoble[i][0])







    """3.     Ingresar un número de sabor y estimar el total de gramos vendidos. 
Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores.
Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. 
Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr."""
    def EstimarSaborMayorCantGramos(self,sabor):
        for i in range(len(self.__ListaSabores)):
            pass