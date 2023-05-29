

from Helado import Helado

class ManejaHelados: 
    
    def __init__(self):
        self.__ListaHelados = []

    def MostrarHeladosTodos(self):
        print("... Mostrando Helados ...")
        for i in range(len(self.__ListaHelados)):
            print(self.__ListaHelados[i])

    def RegistrarHelado(self):
        pass