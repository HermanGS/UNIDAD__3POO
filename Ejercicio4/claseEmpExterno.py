from claseEmpleado import Empleado
class EmpleadoExterno(Empleado):
    __tarea = str
    __fecha_inicio = str
    __fecha_fin = str
    __monto_viatico = 0
    __costo_obra = 0
    __monto_seguro = 0
    __sueldo = 0
    
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = str(tarea)
        self.__fecha_inicio = str(fecha_inicio)
        self.__fecha_fin = str(fecha_fin)
        self.__monto_viatico = int(monto_viatico)
        self.__costo_obra = int(costo_obra)
        self.__monto_seguro = int(monto_seguro)
    
    def getTarea(self):
        return self.__tarea
    def getMontoObra(self):
        return self.__costo_obra
    def getSueldo (self):
        self.__sueldo = (self.__costo_obra - self.__monto_viatico - self.__monto_seguro)
        return (self.__sueldo)    
    def __str__(self):
        print("Dni: {} Nombre: {} Direccion: {} Telefono: {} tarea: {} fecha inicio: {} fecha fin: {} monto viatico: {} costo obra: {} monto seguro: {}".format(self.dni,self.nombre,self.direccion,self.telefono,self.__tarea,self.__fecha_inicio,self.__fecha_fin,self.__monto_viatico, self.__costo_obra,self.__monto_seguro))