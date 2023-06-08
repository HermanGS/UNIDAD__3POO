from Profesor import Profesor
from ListaEnlazada2 import ListaEnlazada2


if __name__ == '__main__':
    print("hola mundo jojo")
    Profesor1 = Profesor(31002008,"Pusineri","Lucas")
    Profesor2 = Profesor(11234432,"Diaz","Monica")
    Profesor3 = Profesor(20201234,"Moreno","Karina")
    
    #print(Profesor2.getDni())

    ListaE = ListaEnlazada2()

    ListaE.agregarElemento(Profesor1)
    ListaE.agregarElemento(Profesor2)
    ListaE.agregarElemento(Profesor3)

    ListaE.recorrerLista()
    """
    ProfesorEncontrado = ListaE.busquedaBanderaDNI(11234432)

    if type(ProfesorEncontrado)== Profesor:
        print("Profesor Encontrado : ",ProfesorEncontrado)
    else:
        print("el profe no es profe")
    """
    #ListaE.eliminarProfesorPorDni2(11234432)
    ListaE.eliminarProfesorPorDni2(20201234)

    print("chorizo")
    for dato in ListaE:
        print(dato)

