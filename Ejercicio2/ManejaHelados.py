
from collections import Counter

from Helado import Helado
from Sabor import Sabor
from ManejaSabores import ManejaSabores



class ManejaHelados: 
    
    def __init__(self):
        self.__ListaHelados = []

    def MostrarHeladosTodos(self):
        if len(self.__ListaHelados) != 0:
            print("... Mostrando Helados ...")
            for i in range(len(self.__ListaHelados)):
                print("Helado ",i+1,"\n",self.__ListaHelados[i])
            print("\n")
        else: 
            print("No hay Helados Registrados")
            print("\n")

    def AñadirHelado(self,helado):
        self.__ListaHelados.append(helado)

    def RegistrarHelado(self,ManejadorSabores):
        print("\n")
        Sabores = []
        id = -1
        while id != 0 :
            print("Ingrese la id del ""Sabor"" a agregar al helado")
            print("Si la respuesta es == 0 (cero) Termina")
            ManejadorSabores.MostrarSabores()
            id = input("Respuesta :  ")
            print("\n")
            while id.isdigit() == False:
                print("ERROR - no es un numero")
                print("Ingrese la id del ""Sabor"" a agregar al helado")
                print("Si la respuesta es == 0 (cero) Termina")
                ManejadorSabores.MostrarSabores()
                id = input("Respuesta :  ")
                print("\n")
            id = int(id)
            Respuesta = ManejadorSabores.BuscarSaborID(id)
            if type(Respuesta) == Sabor:
                Sabores.append(Respuesta)
            else:
                print(" - No se encontró el sabor buscado - o su opcion fue 0 (cero)")
        
        print("Ingrese los Gramos:")
        gramos = input("Respuesta :  ")
        print("Ingrese el precio : ")
        precio = input("Respuesta :  ")
        
        Helao = Helado(gramos,precio,Sabores)
        self.AñadirHelado(Helao)

        #Mostrar Helados Cargados
        print("\n")
        print("\n")
        self.MostrarHeladosTodos()
    
    "2. Mostrar el nombre de los 5 sabores de helado más pedidos."
    
    def Sabores5MasPedidos(self,ManejadorSabores):
        contador_sabores = Counter()
        idx_helado = 0
        while idx_helado < len(self.__ListaHelados):
            helado = self.__ListaHelados[idx_helado]
            idx_sabor = 0
            while idx_sabor < len(helado._Helado__ListaSabores):
                sabor = helado._Helado__ListaSabores[idx_sabor]
                contador_sabores[sabor._Sabor__idSabor] += 1
                idx_sabor += 1
            idx_helado += 1

        top_5_sabores = contador_sabores.most_common(5)

        print("Los 5 sabores más pedidos son:")
        for sabor, cantidad in top_5_sabores:
            print(f"ID del sabor: {sabor}, cantidad de pedidos: {cantidad}")


