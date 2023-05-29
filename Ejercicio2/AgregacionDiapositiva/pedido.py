class Pedido:
    __cantidadPedidos=0
    __idPedido: int
    __numeroMesa: int
    __mozo: object
    __bebidas = []
    __platos = []
    
    
    @classmethod
    def getIdPedido(cls):
        cls.__cantidadPedidos+=1
        return cls.__cantidadPedidos
    
    def __init__(self, numeroMesa, mozo, bebida=None, plato=None):
        self.__numeroMesa=numeroMesa
        self.__mozo=mozo
        self.__idPedido=self.getIdPedido()
        if bebida!=None:
            self.addBebida(bebida,1)
        if plato!=None:
            self.addPlato(plato,1)

    def addBebida(self, bebida, cantidad):
        for i in range(cantidad):
            self.__bebidas.append(bebida)
    def addPlato(self, plato, cantidad):
        for i in range(cantidad):
            self.__platos.append(plato)


    def cerrarPedido(self):
        print('Pedido número: ',self.__idPedido)
        total = 0
        
        print('Bebidas')
        for bebida in self.__bebidas:
            precio = bebida.getPrecio()
            print('{0:20s} {1:4.2f}'.format(bebida.getDenominacion(), precio))
            total+=precio

        print('Platos')
        for plato in self.__platos:
            precio = plato.getPrecio()
            print('{0:20s} {1:4.2f}'.format(plato.getDescripcion(), precio))
            total+=precio

        print('Total a pagar: {0:4.2f}'.format(total))