
class Menu:


    def op1(self,ManejadorFacultades):
        print("Entro al 1 ")
        print("Ingrese el Codigo de Facultad :  ")
        codF = input("Respuesta :  ")
        codF = int(codF)
        ManejadorFacultades.MostrarFacultadYCarrerasPorCodigoF(codF)



    def op2(self,ManejadorFacultades):
        print("Entro al 2 ")
        print("Ingrese un Nombre de Carrera :  ")
        nomC = input("Respuesta :  ")
        nomC = str(nomC)
        ManejadorFacultades.MostrarCodigoFC3(nomC)


    def ElegirOP(self,ManejadorFacultades):
        op = -1
        while op != 0:
            print("-----------------------------------------------------------------------------------")
            print("Ingrese una opcion: (INGRESE 0 (CERO) PARA TERMINAR ) ")
            print("1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.")
            op = input("Respuesta :  ")
            print("\n\n")
            
            while op != '0' and op != '1' and op != '2':
                print("-----------------------------------------------------------------------------------")
                print("Error - OPCION INCORRECTA - Ingrese una opcion: (INGRESE 0 (CERO) PARA TERMINAR )")
                print("1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.\n2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.")  
                op = input("Respuesta :  ")
                print("\n\n")
            op = int(op)
            
            if op == 1:
                self.op1(ManejadorFacultades)

            elif op == 2:
                self.op2(ManejadorFacultades)
            else : 
                print("---FIN PROGRAMA ---")

