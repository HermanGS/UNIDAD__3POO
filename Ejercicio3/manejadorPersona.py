from clasePersona import Persona
class manejadorPersona: 
    __listaPersonas = []
    
    def __init__ (self):
        self.__listaPersonas = []
        
    def agregarPersona (self, persona):
        self.__listaPersonas.append(persona)
              
    def mostrarPersonas(self):
        for i in range(len(self.__listaPersonas)):
            print(self.__listaPersonas[i])
            
   