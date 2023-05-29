



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
        return "id Sabor : {} Nombre : {} Ingredientes : {}".format(self.__idSabor,self.__Nombre,self.__Ingredientes)