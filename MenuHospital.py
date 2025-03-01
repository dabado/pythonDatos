from services import servicio06OracleHospital as service
from models import hospital

class MENUHOSPITAL:
        servicio=service.ServiceOracleHospital()
        def mostrarHospitales():
            servicio=service.ServiceOracleHospital()
            afectados=servicio.muestraHospitales()
            for fila in afectados:
                print(fila)
                #print(fila.numeroHospital, fila.numeroHospital, fila.apellido, fila.especialidad, fila.salario)


        def nuevoHospital():
            servicio=service.ServiceOracleHospital()
            #afectados=servicio.insertarHospital(numeroHospital,nombreHospital, direccion, telefono, numeroCama)
            print("dame un numeroHospital para el Hospital nuevo")
            inumeroHospital=int(input())
            print("dame una nombreHospital para el Hospital nuevo" )
            inombreHospital=input()
            print("dame una direccion para el Hospital nuevo" )
            idireccion=input()
            print("dame un numeroCama para el Hospital nuevo" )
            inumeroCama=int(input())     
            print("dame un telefono para el Hospital nuevo" )
            itelefono=int(input())

            data=servicio.insertarHospital(inumeroHospital,inombreHospital, idireccion, itelefono, inumeroCama)

            print(f"nuevo {data}")
            return data

        def quitarHospital():
            servicio=service.ServiceOracleHospital()
            print("dame un numeroHospital para el Hospital a eliminar")
            inumeroHospital=int(input())
            data=servicio.eliminarHospital(inumeroHospital)
            
            print(f"afectados: {data}")
            return data

        def modificarHospital():
            servicio=service.ServiceOracleHospital()
            print("dame un numero para el inumeroHospital a modificar")
            inumeroHospital=int(input())
            print("dame un inombreHospital para el {inumeroHospital} a modificar")
            inombreHospital=input()
            print("dame un  idireccion a modificar")
            idireccion=input()
            print("dame un telefono el Hospital a modificar")
            itelefono=int(input())
            print("dame un numero de camas para el Hospital a modificar")
            inumeroCama=int(input())
            data=servicio.modificaHospital(inumeroHospital, inombreHospital, idireccion, itelefono, inumeroCama)
            print(f"afectados:{data}")
            return data

