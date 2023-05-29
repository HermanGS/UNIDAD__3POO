


class Helado:
    __Gramos : float
    __Precio : float
    __ListaSabores = []

    def __init__(self,Gramos,Precio,Sabores):
        self.__Gramos = Gramos
        self.__Precio = Precio
        for i in range(len(Sabores)):
            self.__ListaSabores.append(Sabores[i])


    def retornaCadenaSabores(self):
        cadena = ""
        for i in range(len(self.__ListaSabores)):
            cadena = cadena +"|"+ str(self.__ListaSabores[i]) 
        return cadena

    def __str__(self) -> str:
        return "Gramos : {} Precio : {} \n Sabores :{}".format(self.__Gramos,self.__Precio,self.retornaCadenaSabores())

    
