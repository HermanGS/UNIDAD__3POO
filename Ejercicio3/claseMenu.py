from manejadorPersona import manejadorPersona
from clasePersona import Persona
from arregloTaller import arregloTaller
from manejadorInscripcion import manejaInscripcion

class menu: 
    __opcion=None
    
    def mostrarmenu(self):
        persona1 = Persona('Juan Lopez', '43838463', 'Santa Lucia 756 Sur')
        persona2 = Persona('Manuel Perez', '25678999', 'Rivadivia 1900 Norte')
        persona3 = Persona('Lucia Castro', '30090765', 'Chimbas 1918 Norte')
        listaP = manejadorPersona ()
        listaP.agregarPersona(persona1)
        listaP.agregarPersona(persona2)
        listaP.agregarPersona(persona3)
        listaP.mostrarPersonas()
        taller = arregloTaller ()
        taller.carga()
        ins = manejaInscripcion()
        Salir = True
        while Salir:
            print('[1] Cargar los datos de los talleres ')
            print('[2] Inscribir una persona en un taller ')
            print('[3] Consultar inscripción ')
            print('[4] Consultar inscriptos ' )
            print('[5] Registrar pago ')
            print('[6] Guardar inscripciones ')
            print('[0] Salir del programa')
            self.__opcion=input('\nIngrese una opcion: ')
            if self.__opcion=='0':
                Salir = False
            if self.__opcion=='1':
               pass #carga de los talleres 
            if self.__opcion=='2':
                taller.mostrarTaller()
                id1 = int(input("Ingrese el taller elegido 1: "))
                id2 = int(input("Ingrese el taller elegido 2: "))
                tallerElegido1 = taller.TallerPorIndice(id)
                tallerElegido2 = taller.TallerPorIndice(id)
                ins.registrarInscripcion(persona1,tallerElegido1)
                ins.registrarInscripcion(persona2,tallerElegido1)
                ins.MostrarInscripciones()
            if self.__opcion=='3':
                dni = str(input("Ingrese un dni: "))
                ins.consultarInscripcion(dni)