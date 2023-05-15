from Menu import Menu
from Facultad import Facultad
from ManejadorFacultades import ManejadorFacultades

def Menuco(ManejadorFacultades):

    Menuc = Menu()
    Menuc.ElegirOP(ManejadorFacultades)





if __name__ == '__main__':
    print("----- PROGRAMA PRINCIPAL -----")

    MF = ManejadorFacultades()
    MF.IngresoArchivo()


    print("\n \n")
    print("Mostrar Las Facultades y Carreras Cargadas : ...")
    MF.MostrarFacultadesyCarreras()
    print("\n \n")
 

    Menuco(MF)