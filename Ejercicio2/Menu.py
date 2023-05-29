
"""Ejercicio 2
Agregación

La heladería “El Conito” requiere una aplicación para el sector de ventas que registre los helados vendidos de modo que facilite el análisis de estos datos. 

Descripción 

La heladería presenta distintos sabores de helado.
Cada sabor tiene asociado un número que comienza en 1 y es correlativo.
De cada sabor se registra el idSabor, el nombre y los ingredientes.
Los helados se distinguen por el peso expresado en gramos y precio.
Los tipos de helados que se venden son de 100gr, 150 gr, 250 gr, 500 gr y 1000gr.
De un helado vendido se registra el peso del helado y el/los sabor/es pedidos.
 Diagrama de clases

 

 La aplicación que usted debe implementar requiere: 

A.    Implementar las clases del diagrama UML dado.

B.    Definir una clase ManejaSabores que permita manejar los n sabores que la heladería presenta a la venta.

C.    Definir una clase ManejaHelados que registre y gestione a través de una lista los helados vendidos.

D.    Implementar un programa principal que permita:

a.   Cargar los datos de los sabores en una instancia de la clase ManejaSabores. Estos datos se encuentran en el archivo sabores.csv.

b.     A través de un menú de opciones realice las siguientes funcionalidades:

1.     Registrar un helado vendido (instancia de la clase helado).

2.     Mostrar el nombre de los 5 sabores de helado más pedidos.

3.     Ingresar un número de sabor y estimar el total de gramos vendidos. Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores. Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr.

4.  Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.

5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado."""



class Menu:


    def op1(self,ManejadorSabores,ManejadorHelados):
        print("Entro al 1 ")
        ManejadorHelados.RegistrarHelado(ManejadorSabores)

    def op2(self,ManejadorSabores,ManejadorHelados):
        print("Entro al 2 ")
        ManejadorHelados.Sabores5MasPedidos(ManejadorSabores)

    def op3(self,ManejadorSabores,ManejadorHelados):
        print("Entro al 3 ")

    def op4(self,ManejadorSabores,ManejadorHelados):
        print("Entro al 4 ")

    def op5(self,ManejadorSabores,ManejadorHelados):
        print("Entro al 5 ")



    def ElegirOP(self,ManejadorSabores,ManejadorHelados):
        op = -1
        while op != 0 :
            print("<<<--------------------------------------------------------------------------->>>")
            print("Elija una Opcion 1,2,3,4 o 5 Según Desee :  ")
            print("1. Registrar un helado vendido (instancia de la clase helado)\n2. Mostrar el nombre de los 5 sabores de helado más pedidos.\n3. Ingresar un número de sabor y estimar el total de gramos vendidos. Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores. Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr.\n4. Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.\n5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado. ")
            op = input("Respuesta :   ")
            print("\n")
            while op != '1' and op != '2' and op != '3' and op != '4' and op != '5' and op != '0':
                print("<<<--------------------------------------------------------------------------->>>")
                print("ERROR - Opcion Incorrecta : ")
                print("Elija una Opcion 1, 2, 3, 4 o 5 Según Desee :  ")
                print("1. Registrar un helado vendido (instancia de la clase helado)\n2. Mostrar el nombre de los 5 sabores de helado más pedidos.\n3. Ingresar un número de sabor y estimar el total de gramos vendidos. Para un helado se estima la cantidad de gramos de cada sabor dividiendo los gramos del helado en la cantidad de sabores. Por ejemplo, si se vendió un helado de 1000 gr de chocolate, frutilla, limón y americana. Se estima que en este helado se vendió de cada sabor 1000 / 4 = 250gr.\n4. Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño considerando todos los helados vendidos.\n5. Determinar el importe total recaudado por la Heladería, por cada tipo de helado. ")
                op = input("Respuesta :   ")
                print("\n")
            op = int(op)
            
            if op == 1 : 
                self.op1(ManejadorSabores,ManejadorHelados)
            elif op == 2 : 
                self.op2(ManejadorSabores,ManejadorHelados)
            elif op == 3 : 
                self.op3(ManejadorSabores,ManejadorHelados)
            elif op == 4 : 
                self.op4(ManejadorSabores,ManejadorHelados)
            elif op == 5 : 
                self.op5(ManejadorSabores,ManejadorHelados)
            else: 
                print("<<<<<<<<<<<<<<-----------FIN PROGRAMA------------->>>>>>>>>>>>>>")

        
