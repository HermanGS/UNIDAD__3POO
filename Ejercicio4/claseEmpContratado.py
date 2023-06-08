from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fechaInicio = ''
    __fecha_fin = ''
    __horas_trabajadas = 0
    __valor_hora = 0
    __sueldo = 0
    
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas, valor_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = str(fecha_inicio)
        self.__fecha_fin = str(fecha_fin)
        self.__horas_trabajadas = int(horas_trabajadas)
        self.__valor_hora = float(valor_hora)
    
    def getSueldo (self):
        self.__sueldo = self.__horas_trabajadas * self.__valor_hora
        return self.__sueldo 
        
    def actualizarHoras (self, horas):
        self.__horas_trabajadas = self.__horas_trabajadas + horas
        return self.__horas_trabajadas    