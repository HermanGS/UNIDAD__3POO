class TallerCapacitacion:
    __idTaller = int
    __nom = str
    __vacantes = int
    __montoInscripcion = int
    __listaInscripciones = []
    
    def __init__(self, idTaller, nom, vacantes, monto):
        self.__idTaller = str(idTaller)
        self.__nom = str(nom)
        self.__vacantes = int(vacantes)
        self.__montoInscripcion =int(monto)
        
    def getId(self):
        return self.__idTaller
    def getNom(self):
        return self.__nom
    def getVacantes (self):
        return self.__vacantes
    def getMonto (self):
        return self.__montoInscripcion
    def actualizarVacante (self):
        self.__vacantes -= 1
    def __str__(self) -> str:
        return "Id : {} Nombre : {} Vacantes : {} Monto : {}".format(self.__idTaller,self.__nom,self.__vacantes,self.__montoInscripcion)