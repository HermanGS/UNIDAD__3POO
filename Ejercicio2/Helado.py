


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
            cadena = cadena +"\n"+ str(self.__ListaSabores[i]) 
        return cadena

    def __str__(self) -> str:
        return "Gramos : {} Precio : {} \n Sabores :{}".format(self.__Gramos,self.__Precio,self.retornaCadenaSabores())

    def contarRepitenciaSaborCH(self,sabor):
        contador = 0
        for i in range(len(self.__ListaSabores)):
            if sabor == self.__ListaSabores[i]:
                contador = contador + 1
        valor = contador
        print("Contador helado : ",contador)
        return valor
    
    


    def contarGramos(self):
        if len(self.__ListaSabores):
            pass

    