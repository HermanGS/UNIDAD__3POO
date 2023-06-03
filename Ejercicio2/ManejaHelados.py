
from collections import Counter

from Helado import Helado
from Sabor import Sabor
from ManejaSabores import ManejaSabores



class ManejaHelados: 
    
    def __init__(self):
        self.__ListaHelados = []



    #Mostrar
    def MostrarHeladosTodos(self):
        if len(self.__ListaHelados) != 0:
            print("... Mostrando Helados ...")
            for i in range(len(self.__ListaHelados)):
                print("Helado ",i+1,"\n",self.__ListaHelados[i])
            print("\n")
        else: 
            print("No hay Helados Registrados")
            print("\n")

    def MostrarOpciones(self):
        print("Ingrese los Gramos:")
        """Los tipos de helados que se venden son de 100gr, 150 gr, 250 gr, 500 gr y 1000gr."""
        print("1. 100  Gramos \n2. 150  Gramos \n3. 250  Gramos \n4. 500  Gramos \n5. 1000 Gramos")
        



    def AñadirHelado(self,helado):
        self.__ListaHelados.append(helado)

    #ITEM 1
    def RegistrarHelado(self,ManejadorSabores):
        print("\n")
        Sabores = []
        id = -1
        while id != 0 :
            print("Ingrese la id del ""Sabor"" a agregar al helado")
            print("Si la respuesta es == 0 (cero) Termina")
            ManejadorSabores.MostrarSabores()
            id = input("Respuesta :  ")
            print("\n")
            while id.isdigit() == False:
                print("ERROR - no es un numero")
                print("Ingrese la id del ""Sabor"" a agregar al helado")
                print("Si la respuesta es == 0 (cero) Termina")
                ManejadorSabores.MostrarSabores()
                id = input("Respuesta :  ")
                print("\n")
            id = int(id)                                            # CAST 
            Respuesta = ManejadorSabores.BuscarSaborID(id)
            if type(Respuesta) == Sabor:
                Sabores.append(Respuesta)
                print("\nSabor [ {} ] Añadido al Helado \n".format(Respuesta))
            else:
                print(" - No se encontró el sabor buscado - o su opcion fue 0 (cero)")
        
        
        #Carga de gramos vieja


        """
        print("Ingrese los Gramos:")
        gramos = input("Respuesta :  ")
        gramos = float(gramos)                        # Había que modificar acá , haciendo un casteo para que sean de los tipos adecuados para que funcionase el ITEM 3
         
        print("Ingrese el precio : ")
        precio = input("Respuesta :  ")
        precio = float(precio)
        """
        "Los tipos de helados que se venden son de 100gr, 150 gr, 250 gr, 500 gr y 1000gr."
        





        #Modifiqué la carga de los gramos porque parece ser que los tipos de helados(cantidad gramos solo pueden ser 5)
        #Es solo un menú con opciones, para facilitar la carga
        self.MostrarOpciones()
        gramos = input("Respuesta :  ")
        while gramos != '1' and gramos != '2' and gramos != '3' and gramos != '4' and gramos != '5':
            print("\nERROR - Elija entre las opciones : \n")
            self.MostrarOpciones()
            gramos = input("Respuesta :  ")

        if gramos == '1': gramos = '100'
        elif gramos == '2' : gramos = '150'
        elif gramos == '3' : gramos = '250'
        elif gramos == '4' : gramos = '500'
        else : gramos = '1000'

        gramos = float(gramos)
        print("\nGramos ingresados : ",gramos)
        
        print("\nIngrese el precio : ")
        precio = input("Respuesta :  ")
        precio = float(precio)
        
        Helao = Helado(gramos,precio,Sabores)
        self.AñadirHelado(Helao)

        #Mostrar Helados Cargados
        print("\n")
        print("\n")
        self.MostrarHeladosTodos()
    
    "2. Mostrar el nombre de los 5 sabores de helado más pedidos."
    




    #ITEM 2
    def ContarRepitenciaSabor(self,sabor):
        contadorTotal = 0
        for i in range(len(self.__ListaHelados)):
            #print("Interno CT",contadorTotal,"Interno CdeHelado",self.__ListaHelados[i].contarRepitenciaSaborCH(sabor))
            #print("ContadorTotal + Contador de Helado  = ",contadorTotal + self.__ListaHelados[i].contarRepitenciaSaborCH(sabor))
            #contadorTotal = contadorTotal + self.__ListaHelados[i].contarRepitenciaSaborCH(sabor)
            contadorTotal = self.__ListaHelados[i].contarRepitenciaSaborCH(sabor)
        #print("Contador Total Helados : ",contadorTotal)
        return contadorTotal
    

    #ITEM 3
    def ContarGramosPorSaborManejadorHelado(self,sabor):
        contadorGramos = 0
        for i in range(len(self.__ListaHelados)):
            contadorGramos = contadorGramos + self.__ListaHelados[i].contarGramosPorSaborHelado(sabor)                    #opcion 1 , ver si funciona ... Funciona bien
            #contadorGramos = self.__ListaHelados[i].contarGramosPorSaborHelado(sabor)                    #opcion 2 , ver si funciona ... Saca la mitad de la opcion anterior

        print("Contador Total GRAMOS : ",contadorGramos)
        return contadorGramos
    

    #ITEM 4   Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos
    def pito(self):
        pass