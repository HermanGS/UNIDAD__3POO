
from clases import Bebida
from clases import Plato
from clases import Mozo
from pedido import Pedido


def testAgregacion():
    bebida = Bebida('Coca cola','1/2 litro',750)
    bebida1 = Bebida('Aquarius', '1/2 litro',500)
    plato = Plato('Lomo especial',3250)
    papas = Plato('Papa frita chica',1250)
    pizza = Plato('Pizza especial', 3900)
    mozo1 = Mozo(1, 'López', 'Carlos')
    pedido1 = Pedido(1, mozo1, bebida, plato)
    pedido1.addBebida(bebida1,2)
    pedido1.addPlato(papas,1)
    pedido1.addPlato(plato,3)
    pedido1.cerrarPedido()
    del pedido1
    pedido2 = Pedido(2, mozo1, bebida1, papas)
    pedido2.addBebida(bebida,2)
    pedido2.addPlato(pizza,1)
    pedido2.cerrarPedido()


if __name__=='__main__':
    testAgregacion()