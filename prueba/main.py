from Profesor import Profesor
from ListaEnlazada2 import ListaEnlazada2


if __name__ == '__main__':
    print("hola mundo jojo")
    Profesor1 = Profesor(31002008,"Pusineri","Lucas")
    Profesor2 = Profesor(11234432,"Diaz","Monica")
    Profesor3 = Profesor(20201234,"Moreno","Karina")
    Profesor4 = Profesor(42711885,"Moreno","Camila")
    Profesor5 = Profesor(42711885,"Miriani","Renzo")
    #print(Profesor2.getDni())

    ListaE = ListaEnlazada2()

    #ListaE.append(Profesor1)
    #ListaE.append(Profesor2)
    #ListaE.append(Profesor3)
    
    ListaE.agregarElemento(Profesor1)
    ListaE.agregarElemento(Profesor2)
    ListaE.agregarElemento(Profesor3)
    ListaE.agregarElemento(Profesor4)

    print("Cuando se Agrega el elemento de la forma vieja luego de usar la nueva")
    #ListaE.agregarElemento(Profesor4)
    print("Imprimir cabeza : ")
    ListaE.ImprimirElementoCabeza()


    print("Recorrer Lista (Solo muestra) :")
    ListaE.recorrerLista()

    """
    ProfesorEncontrado = ListaE.busquedaBanderaDNI(11234432)

    if type(ProfesorEncontrado)== Profesor:
        print("Profesor Encontrado : ",ProfesorEncontrado)
    else:
        print("el profe no es profe")
    """
    #ListaE.eliminarProfesorPorDni2(11234432)
    #ListaE.eliminarProfesorPorDni2(20201234)

    #tope  = ListaE.retornaTOPE()
    """
    for i in range(tope):
        print(ListaE[i])
    """
    print("Recorrer Lista 2 Aux queda apuntado al Último Elemento de la Lista  :")
    ListaE.recorrerLista2()


    print("Agregar al Final V2 :")
    ListaE.AgregarAlFinal(Profesor4)
    #ListaE.AgregarAlFinal(Profesor4)

    print("Recorrer Lista 1 :")
    ListaE.recorrerLista()


    long = ListaE.retornaLongitud()
    print("Longitud de la lista => ",long)
    print("Por favor ingrese un numero entre 1 y ",long)

    pos = input("Ingrese una posicion para añadir al nuevo profesor   :   ")
    pos = int(pos)
    ListaE.insertarelemento(pos,Profesor5)


    print("- Lista Con iterador - chorizo - Mostrar -")
    for dato in ListaE:
        print(dato)

    
