


class Carrera:
    __Codigo : int
    __Nombre : str
    __FechaInicio : str
    __Duracion : str
    __Titulo : str

    def __init__(self,Codigo,Nombre,fechainicio,duracion,titulo) -> None:
        self.__Codigo = Codigo
        self.__Nombre = Nombre
        self.__FechaInicio = fechainicio
        self.__Duracion = duracion
        self.__Titulo = titulo

    def __str__(self) -> str:
        return "Codigo : {} Nombre : {} FechaInicio : {} Duración : {} Titulo : {}".format(self.__Codigo,self.__Nombre,self.__FechaInicio,self.__Duracion,self.__Titulo)
    
    def Nombre_y_Duracion(self):
        print("Nombre : {} Duración : {}".format(self.__Nombre,self.__Duracion))


    def retornaCodigo(self):
        return self.__Codigo
    
    def retornaNombre(self):
        return self.__Nombre
    
