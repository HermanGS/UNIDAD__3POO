

class Profesor:
    __dni : int
    __apellido : str
    __nombre : str


    def __init__(self,dni,apellido,nombre):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre


    def __str__(self) -> str:
        return "dni : {} apellido : {} nombre : {}".format(self.__dni,self.__apellido,self.__nombre)
    
    def getDni(self):
        return self.__dni
    