from services import servicio07OracleEmpleado as service
from models import empleado

class MENUEmpleado:
        servicio=service.ServiceOracleEmpleado()
        def mostrarEmpleadoes():
            servicio=service.ServiceOracleEmpleado()
            afectados=servicio.muestraEmpleadoes()
            for fila in afectados:
                print(fila)
                #print(fila.numeroEmpleado, fila.numeroEmpleado, fila.apellido, fila.especialidad, fila.salario)


        def nuevoEmpleado():
            servicio=service.ServiceOracleEmpleado()
            #afectados=servicio.insertarEmpleado(numeroEmpleado,nombreEmpleado, direccion, telefono, numeroCama)
            print("dame un numeroEmpleado para el Empleado nuevo")
            inumeroEmpleado=int(input())
            print("dame una nombreEmpleado para el Empleado nuevo" )
            inombreEmpleado=input()
            print("dame una direccion para el Empleado nuevo" )
            idireccion=input()
            print("dame un numeroCama para el Empleado nuevo" )
            inumeroCama=int(input())     
            print("dame un telefono para el Empleado nuevo" )
            itelefono=int(input())

            data=servicio.insertarEmpleado(inumeroEmpleado,inombreEmpleado, idireccion, itelefono, inumeroCama)

            print(f"nuevo {data}")
            return data

        def quitarEmpleado():
            servicio=service.ServiceOracleEmpleado()
            print("dame un numeroEmpleado para el Empleado a eliminar")
            inumeroEmpleado=int(input())
            data=servicio.eliminarEmpleado(inumeroEmpleado)
            
            print(f"afectados: {data}")
            return data

        def modificarEmpleado():
            servicio=service.ServiceOracleEmpleado()
            print("dame un numero para el inumeroEmpleado a modificar")
            inumeroEmpleado=int(input())
            print("dame un inombreEmpleado para el {inumeroEmpleado} a modificar")
            inombreEmpleado=input()
            print("dame un  idireccion a modificar")
            idireccion=input()
            print("dame un telefono el Empleado a modificar")
            itelefono=int(input())
            print("dame un numero de camas para el Empleado a modificar")
            inumeroCama=int(input())
            data=servicio.modificaEmpleado(inumeroEmpleado, inombreEmpleado, idireccion, itelefono, inumeroCama)
            print(f"afectados:{data}")
            return data
