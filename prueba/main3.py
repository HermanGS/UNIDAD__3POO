from Profesor import Profesor
from ListaEnlazada2 import ListaEnlazada2


if __name__ == '__main__':
    print("\n --------- MAIN V2 --------- \n")
    Profesor1 = Profesor(31002008,"Pusineri","Lucas")
    Profesor2 = Profesor(11234432,"Diaz","Monica")
    Profesor3 = Profesor(20201234,"Moreno","Karina")
    Profesor4 = Profesor(42711885,"Moreno","Camila")
    Profesor5 = Profesor(42711885,"Miriani","Renzo")
    #print(Profesor2.getDni())

    ListaE = ListaEnlazada2()



    ListaE.recorrerLista()


    long = ListaE.retornaLongitud()
    print("Longitud de la lista => ",long)
    print("Por favor ingrese un numero entre 1 y ",long)

    pos = input("Ingrese una posicion para añadir al nuevo profesor   :   ")
    pos = int(pos)
    ListaE.insertar(pos,Profesor5)



    ListaE.recorrerLista()