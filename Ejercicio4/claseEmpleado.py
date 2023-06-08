class Empleado:
    __DNI = ''
    __nombre = ''
    __direc = ''
    __telefono = ''
    __sueldo = int 
    
    def __init__(self, dni, nom, direc, tel):
        self.__DNI = str(dni)
        self.__nombre = str(nom)
        self.__direc = str(direc)
        self.__telefono = str(tel)
    
    def getDni (self):
        return self.__DNI   
    def getNombre (self):
        return self.__nombre
    def getTelefono (self):
        return self.__telefono
    def getDirec (self):
        return self.__direc  