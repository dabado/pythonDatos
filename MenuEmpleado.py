
from services import servicioOracleEmpleado as service
from models import empleado 

class MENUEMPLEADO:
    #servicio=service.ServiceOracleEmpleado()

    def mostrarEmpleado():
        servicio=service.ServiceOracleEmpleado()
        afectados=servicio.muestraEmpleado()
        for fila in afectados:
            print( fila)

    def nuevoEmpleado():
            servicio=service.ServiceOracleEmpleado()
            #afectados=servicio.insertarEmpleado(emp_no, apellido , oficio , dir , fecha_alta , salario, comision, dept_no)
            print("dame un numeroEmpleado para el Empleado nuevo")
            emp_no=int(input())
            print("dame un apellido para el Empleado nuevo" )
            apellido=input()
            print("dame un oficio para el Empleado nuevo" )
            oficio=input()
            print("dame un dir para el Empleado nuevo" )
            dir=int(input())     
            print("dame una fecha_alta para el Empleado nuevo" )
            fecha_alta=input()
            print("dame un salario para el Empleado nuevo" )
            salario=int(input())     
            print("dame la comision para el Empleado nuevo" )
            comision=int(input())     
            print("dame el departamento para el Empleado nuevo" )
            dept_no=int(input())  
            data=servicio.insertarEmpleado(emp_no, apellido , oficio , dir , fecha_alta , salario, comision, dept_no)

            print(f"nuevo {data}")
            return data

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
        afectados=servicio.modificaEmpleado(numero, nombre, localidad )
        print(f"Empleado modificado numero {numero}: ,afectado: {afectados}")
