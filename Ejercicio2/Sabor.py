



class Sabor:
    __CantidadSabores = 0
    __Nombre : str
    __Ingredientes: str

    @classmethod
    def getIdSabor(cls):
        cls.__CantidadSabores += 1 
        return cls.__CantidadSabores

    def __init__(self,idSabor,Nombre,Ingredientes):
        self.__idSabor = self.getIdSabor()
        self.__Nombre = Nombre
        self.__Ingredientes = Ingredientes

    def __str__(self) -> str:
        return "(id : {} Nombre : {} Ingredientes : {})".format(self.__idSabor,self.__Nombre,self.__Ingredientes)
    
    # 3 retornas ID , NOMBRE, INGREDIENTES

    def retornaID(self):
        return self.__idSabor
    
    def retornaNombre(self):
        return self.__Nombre

    def retornaIngredientes(self):
        return self.__Ingredientes

    def __eq__(self, __otro: object) -> bool:
        bandera = False
        if type(self) == type(__otro):
            if self.__idSabor == __otro.retornaID() and self.__Nombre == __otro.retornaNombre() and self.__Ingredientes == __otro.retornaIngredientes():
                #print("self : ",self , "\n y otro : ",__otro) 
                bandera = True
        return bandera
