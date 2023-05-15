
import csv
from Facultad import Facultad
from Carrera import Carrera

class ManejadorFacultades:
    __ListaFacultades : list

    def __init__(self) -> None:
        self.__ListaFacultades =  []


    def IngresoArchivo(self):
        nombreArchivo = 'Facultades.csv'
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo,delimiter = ',')

        filaFacultad = next(reader)
        print("filaFacultad :    ",filaFacultad)

        bandera  = True
        

        while bandera :
            
            #Carga de Facultad
            CodigoFacultad = int(filaFacultad[0])
            NombreFacultad = str(filaFacultad[1])
            Direccion = str(filaFacultad[2])
            Localidad = str(filaFacultad[3])
            Telefono = str(filaFacultad[4])
            listaCarreras = []
            
            filaCarrera = next(reader)
            
            while bandera and filaFacultad[0] == filaCarrera[0]:
                #Carga de Carrera
                
                print("filaCarrera :    ",filaCarrera)

                CodigoCarrera = int(filaCarrera[1])
                NombreCarrera = str(filaCarrera[2])
                FechaInicio = str(filaCarrera[3])
                Duracion = str(filaCarrera[4])
                Titulo = str(filaCarrera[5])

                CarreraTemp = Carrera(CodigoCarrera,NombreCarrera,FechaInicio,Duracion,Titulo) #Objeto Carrera

                listaCarreras.append(CarreraTemp)  #ATRIBUTO DE LA FACULTAD

                try:
                    filaCarrera = next(reader) #Intenta pasar a la linea siguiente, lo que puede dar error (iterar en carreras)
                
                except StopIteration : # Para que TERMINE TODO si es que llegó al final del archivo (pq genera error)
                    bandera = False

            filaFacultad = filaCarrera #Cuando sale del bucle, es porque no es una carrera sino una facultad ...
            #print(filaFacultad)                           # filaFacultad[0] != filaCarrera[0]
            FacultadTemp = Facultad(CodigoFacultad,NombreFacultad,Direccion,Localidad,Telefono,listaCarreras)
            self.__ListaFacultades.append(FacultadTemp)

        print("--- Fin de Ingreso de Facultades y de Carreras ---")
        archivo.close()


    def MostrarFacultadesyCarreras(self):
        for i in range(len(self.__ListaFacultades)):
            print("\nFacultad : \n",self.__ListaFacultades[i])
            self.__ListaFacultades[i].MostrarCarreras()
             

    """1. Ingresar el código  de una facultad
    y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad."""

    def MostrarFacultadYCarrerasPorCodigoF(self,codigoF):
        if type(codigoF) == int:
            if codigoF < 0 or codigoF > len(self.__ListaFacultades):
                print("Error - Codigo de Facultad Fuera de Rango")
            else:
                self.__ListaFacultades[codigoF-1].MostrarCarrerasNombre_y_Duracion()
        else : 
            print("El codigo de Facultad Ingresado no es entero")


    """2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), 
nombre y localidad de la facultad donde esta se dicta."""

 
    def MostrarCodigoFC1(self,nombre): # NO FUNCIONA
        i = 0
        while i < len(self.__ListaFacultades) and self.__ListaFacultades[i].BuscarCarreraPorNombre(nombre) != None:
            

            i=i+1

        if i < len(self.__ListaFacultades):
            
            indice = self.__ListaFacultades[i].BuscarCarreraPorNombre(nombre)
            print(indice)
            print("Codigo : ({},{})".format(self.__ListaFacultades[i].retornaCodigo(), self.__ListaFacultades[i].retornaCodigoCarreraPorIndice(indice) ))
        else:
            print("No se encontro dicha Carrera en ninguna Facultad")




    def MostrarCodigoFC2(self,nombre): #FUNCIONA Pero no aplica bien la metodología orientada a objetos (Me estoy complicando)
        i = 0
        bandera = False
        while i < len (self.__ListaFacultades) and bandera != True:
            listaCarreras = self.__ListaFacultades[i].retornaListaCarreras()
            
            j = 0
            while j < len(listaCarreras) and listaCarreras[j].retornaNombre() != nombre:
                j = j + 1
            
            if j < len(listaCarreras):
                bandera = True

                indiceFacultad = i
                codigoFacultad = self.__ListaFacultades[i].retornaCodigo()

                indiceCarrera = j
                codigoCarrera = listaCarreras[j].retornaCodigo()

            i = i + 1


        print("Codigo : ({},{})".format(codigoFacultad, codigoCarrera ))
        print("Nombre Facultad : {} \nLocalidad : {}".format(self.__ListaFacultades[indiceFacultad].retornaNombre(),self.__ListaFacultades[indiceFacultad].retornaLocalidad()))



    def MostrarCodigoFC3(self,nombre): #funca mejor, aplica mucho mejor la metodología (Cada parte la hace quien le corresponde)
        i = 0
        bandera = False
        while i < len (self.__ListaFacultades) and bandera != True:
            """
            listaCarreras = self.__ListaFacultades[i].retornaListaCarreras()
            
            j = 0
            while j < len(listaCarreras) and listaCarreras[j].retornaNombre() != nombre:
                j = j + 1
            
            if j < len(listaCarreras):
                bandera = True

                indiceFacultad = i
                codigoFacultad = self.__ListaFacultades[i].retornaCodigo()

                indiceCarrera = j
                codigoCarrera = listaCarreras[j].retornaCodigo()
            """

            CarreraT = self.__ListaFacultades[i].BuscarCarreraPorNombre(nombre)
            print("tipo de carrera : ",type(CarreraT))
            if type(CarreraT) == Carrera:
                print("Si encontro la Carrera Buscada")
                bandera = True

                indiceFacultad = i
                codigoFacultad = self.__ListaFacultades[i].retornaCodigo()
            

            i = i + 1

        if bandera:
            print("Codigo : ({},{})".format(codigoFacultad, CarreraT.retornaCodigo() ))
            print("Nombre Facultad : {} \nLocalidad : {}".format(self.__ListaFacultades[indiceFacultad].retornaNombre(),self.__ListaFacultades[indiceFacultad].retornaLocalidad()))
        else : 
            print("No se encontro la Carrera Buscada")

