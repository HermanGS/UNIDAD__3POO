class Inscripcion:
    __fechaInscripcion = str
    __pago = bool
    __persona = object 
    __taller = object
    
    def __init__ (self, fecha, persona, taller):
        self.__fechaInscripcion = fecha
        self.__pago = False
        self.__persona = persona
        self.__taller = taller
        
    def setPago (self):
        self.__pago = True
        
    def __str__(self) -> str:
        return "Fecha : {} Pago : {} \nPersona : {}\nTaller elegido : {}".format(self.__fechaInscripcion,self.__pago,self.__persona,self.__taller)    
    
    def Persona(self):
        return self.__persona
    
    def Taller(self):
        return self.__taller