
from services import servicio07OracleEmpleado as service
from models import empleado 

class MENUEMPLEADO:
    def nuevoEmpleado():
        servicio = service.ServiceOracleEmpleado()
        print("dame un numero para el departamento nuevo")
        deptno=int(input())
        print("dame un nombre para el departamento nuevo")
        dname=input()
        print("dame una localizacion para el departamento nuevo" )
        LOCA=input()
        afectados=servicio.insertarEmpleado(deptno, dname, LOCA)
        print(f"Empleado insertado: {afectados}")


    def BuscarOracleEmpleadoID():
        servicio = service.ServiceOracleEmpleado()
        print("dame un numero para el departamento a buscar")
        deptno=int(input())
        afectados=servicio.buscarEmpleadoNumero(deptno)
        print(f"Empleado encontrado: {deptno}, {afectados}")
        return afectados

    def borrarEmpleadoNumero():
        servicio=service.ServiceOracleEmpleado()
        print("dame un numero para el departamento a Borrar")
        numero=int(input())
        afectados=servicio.eliminarEmpleado(numero)
        print(f"Empleado eliminado numero {numero}: ,afectado: {afectados}")

    def modificarEmpleadoNumero():
        servicio=service.ServiceOracleEmpleado()
        print("dame un numero para el departamento a modificar")
        numero=int(input())
        print("dame un nombre para el departamento a modificar")
        nombre=input()
        print("dame una localidad para el departamento a modificar")
        localidad=input()
        afectados=servicio.modificarEmpleado(numero, nombre, localidad )
        print(f"Empleado modificado numero {numero}: ,afectado: {afectados}")

    def mostrarEmpleado():
        servicio=service.ServiceOracleEmpleado()
        afectados=servicio.muestraEmpleado()
        for fila in afectados:
            print( fila.numero, fila.nombre , fila.localidad)
