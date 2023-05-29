class Bebida:
    __denominacion: str
    __presentacion: str
    __precio: float
    def __init__(self, denominacion, presentacion, precio):
        self.__denomiancion=denominacion
        self.__presentacion=presentacion
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    def getDenominacion(self):
        return self.__denomiancion



class Plato:
    __descripcion: str
    __precio: float
    def __init__(self, descripcion, precio):
        self.__descripcion=descripcion
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    def getDescripcion(self):
        return self.__descripcion

class Mozo:
    __idMozo: int
    __apellido: str
    __nombre :str
    def __init__(self, idMozo, apellido, nombre):
        self.__idMozo=idMozo
        self.__apellido=apellido
        self.__nombre=nombre