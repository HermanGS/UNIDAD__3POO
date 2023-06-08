from claseManejador import manejaEmpleados

class Menu:
    __opcion = None
    def muestraMenu(self):
        band = True
        tamaño = 7
        emp = manejaEmpleados(tamaño)
        emp.carga()
        while band:
            print('==== MENU DE OPCIONES ====\n')
            print('[1] Registrar horas: Ingresar el DNI de un empleado y la cantidad de horas trabajadas en el día de la fecha e incrementar la cantidad de las horas trabajadas del empleado.')
            print('[2] Total de tarea: Dada una tarea mostrar el monto a pagar para ella.')
            print('[3] Ayuda Económica: La empresa dará una ayuda solidaria a los empleados cuyo sueldo sea inferior a $150000; listar nombre, dirección y DNI de los empleados que les corresponde la ayuda.')
            print('[4] Calcular sueldo: Mostrar nombre, teléfono y sueldo a cobrar de todos los empleados.')
            self.__opcion = input('Ingrese opcion: ')
            if self.__opcion == '0':
                band == False
                print('Saliendo del programa...')
            if self.__opcion == '1':
                dni =int(input("Ingrese un dni: "))
                emp.buscarDni(dni)
            if self.__opcion == '2':
                tarea = str(input("Ingrese una tarea: "))
                emp.muestraMontoObra(tarea)    
            if self.__opcion == '3':
                emp.ayudaEconomica()  
            if self.__opcion == '4':
                emp.mostrarSueldos()    
            