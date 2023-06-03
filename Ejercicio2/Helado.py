


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
        #print("Contador helado : ",contador)
        return valor
    
    


    def contarGramosPorSaborHelado(self,sabor): 
        if len(self.__ListaSabores) != 0: # Para no dividir los gramos por 0 
                                                         
            # funcion : 
            
            gramosCadaSabor = self.__Gramos / len(self.__ListaSabores) # Obtener el peso de cada bocha xd
            repeticionesSabor = 0                                      # Contador repeticiones de cada sabor
            for i in range(len(self.__ListaSabores)):
                if sabor == self.__ListaSabores[i]:
                    repeticionesSabor = repeticionesSabor + 1    # cuento 
            return repeticionesSabor * gramosCadaSabor           # cantidad de bochas * cuanto pesa cada una = [ total de gramos de un sabor en un helado ]
        
        
        else: print("No tiene sabores este helado") 
    