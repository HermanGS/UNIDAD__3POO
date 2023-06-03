import csv
from Sabor import Sabor

class ManejaSabores: 
    
    def __init__(self):
        self.__ListaSabores = []


    #Funcion Ingreso de datos
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

    #FUNCIONES MOSTRAR
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

    def MostrarNombreDeSabores(self):
        for i in range(len(self.__ListaSabores)):
            if type(self.__ListaSabores[i]) == Sabor:
                print(self.__ListaSabores[i].retornaID(),self.__ListaSabores[i].retornaNombre())






    #FUNCIONES BUSCAR
    def BuscarSaborID(self,id):
        i = 0
        while i < len(self.__ListaSabores) and self.__ListaSabores[i].retornaID() != id:
            i = i + 1
        if i <len(self.__ListaSabores):
            return self.__ListaSabores[i]
        #print("No se encontró el sabor Buscado por ID")





    #Lo que no hay que hacer xd
    def retornaCantidadSabores(self):
        return len(self.__ListaSabores)
   


    # ITEM 2
    def Sabores5MasPedidosOriginal(self,ManejadorHelados):
        listaContadores = []
        for i in range(len(self.__ListaSabores)):
            CantidadTotal = ManejadorHelados.ContarRepitenciaSabor(self.__ListaSabores[i])
            #listaContadores.append(CantidadTotal - CantidadTotal/2)
            listaContadores.append(CantidadTotal)


        listaDoble = list(zip(self.__ListaSabores,listaContadores))   # zip LISTA de sabor con su valor de repetición
        
        
        #listaContadores.sort(reverse = True)                          # Ordenamiento de la lista de los valores de repetición nada más
       

        # lo muestro directamente abajo, esto ya no lo uso
        """
        if len(listaContadores) >= 5:
            print("Los 5 sabores más Pedidos : ")
            for i in range(5):                         
                print(listaContadores[i])
        else :
            print("Los 5 sabores más Pedidos : (No llegan a 5)") 
            for i in listaContadores:
                print(i)
        """


        listaDoble.sort(key = lambda x : x[1] ,reverse = True) # ordenamiento de la lista Doble que viene de zip

        for i in range(len(listaDoble)):                       # Mostrar la lista 
            print("El Sabor {}   ... Se repite una cantida de veces de : {}".format(listaDoble[i][0],listaDoble[i][1]))

    






    """3.     Ingresar un número de sabor y estimar el total de gramos vendidos. 
Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores.
Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. 
Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr."""
    
    #ITEM 3
    def EstimarSaborMayorCantGramos(self,idsabor,ManejadorHelado):
        # viene un número de sabor como parámetro 
            Sabore = self.BuscarSaborID(idsabor)
            if type(Sabore) == Sabor:
                
                TotalGramosSabor = ManejadorHelado.ContarGramosPorSaborManejadorHelado(Sabore)
                print("Total de Gramos del sabor [ {} ]  =>  {} gramos ".format(Sabore.retornaNombre(),TotalGramosSabor))
            else : print("No se encontró el Sabor buscado  - ID probablemente incorrecta")