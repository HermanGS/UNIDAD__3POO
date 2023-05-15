from Carrera import Carrera


class Facultad:

    __Codigo: int
    __Nombre: str
    __Direccion: str
    __Localidad: str
    __Telefono: str
    __CarreraTemporal: object
    __ListaCarreras: list

    def __init__(self, codigo, nombre, direccion, localidad, telefono, listaDeCarrerasAfuera):
        self.__Codigo = codigo
        self.__Nombre = nombre
        self.__Direccion = direccion
        self.__Localidad = localidad
        self.__Telefono = telefono
        self.__ListaCarreras = []

        for i in range(len(listaDeCarrerasAfuera)):
            self.__ListaCarreras.append(listaDeCarrerasAfuera[i])

    def __str__(self):
        return "Codigo : {} Nombre : {} Dirección : {}\nLocalidad : {} Telefono : {}".format(self.__Codigo, self.__Nombre, self.__Direccion, self.__Localidad, self.__Telefono)

    def retornaCodigo(self):
        return self.__Codigo

    def retornaNombre(self):
        return self.__Nombre

    def retornaLocalidad(self):
        return self.__Localidad

    def retornaListaCarreras(self):
        return self.__ListaCarreras

    def MostrarCarreras(self):
        print("\nCarreras : \n")
        for i in range(len(self.__ListaCarreras)):
            print(self.__ListaCarreras[i])

    def MostrarCarrerasNombre_y_Duracion(self):
        print("\nCarreras : \n")
        for i in range(len(self.__ListaCarreras)):
            self.__ListaCarreras[i].Nombre_y_Duracion()

    # no se usa ---

    def retornaCodigoCarreraPorIndice(self, indice):
        return self.__ListaCarreras[indice].retornaCodigo()
    # ---
    def BuscarCarreraPorNombre(self, nombre):
        i = 0
        while i < len(self.__ListaCarreras) and self.__ListaCarreras[i].retornaNombre() != nombre:
            i += 1

        if i < len(self.__ListaCarreras):
            return self.__ListaCarreras[i]



