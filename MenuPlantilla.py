
from services import servicioOraclePlantilla as service
from models import plantilla 

class MENUPLANTILLA:
        servicio=service.ServiceOraclePlantilla()
        def muestraPlantilla():
            servicio=service.ServiceOraclePlantilla()
            afectados=servicio.muestraPlantilla()
            for fila in afectados:
                print(fila)
                #print(fila.numeroPlantilla, fila.numeroPlantilla, fila.apellido, fila.especialidad, fila.salario)


        def nuevoPlantilla():
            servicio=service.ServiceOraclePlantilla()
            #afectados=servicio.insertarPlantilla(numeroPlantilla,nombrePlantilla, direccion, telefono, numeroCama)
            print("dame un numeroPlantilla para el Plantilla nuevo")
            inumeroPlantilla=int(input())
            print("dame una nombrePlantilla para el Plantilla nuevo" )
            inombrePlantilla=input()
            print("dame una direccion para el Plantilla nuevo" )
            idireccion=input()
            print("dame un numeroCama para el Plantilla nuevo" )
            inumeroCama=int(input())     
            print("dame un telefono para el Plantilla nuevo" )
            itelefono=int(input())

            data=servicio.insertarPlantilla(inumeroPlantilla,inombrePlantilla, idireccion, itelefono, inumeroCama)

            print(f"nuevo {data}")
            return data

        def quitarPlantilla():
            servicio=service.ServiceOraclePlantilla()
            print("dame un numeroPlantilla para el Plantilla a eliminar")
            inumeroPlantilla=int(input())
            data=servicio.eliminarPlantilla(inumeroPlantilla)
            
            print(f"afectados: {data}")
            return data

        def modificarPlantilla():
            servicio=service.ServiceOraclePlantilla()
            print("dame un numero para el inumeroPlantilla a modificar")
            inumeroPlantilla=int(input())
            print("dame un inombrePlantilla para el {inumeroPlantilla} a modificar")
            inombrePlantilla=input()
            print("dame un  idireccion a modificar")
            idireccion=input()
            print("dame un telefono el Plantilla a modificar")
            itelefono=int(input())
            print("dame un numero de camas para el Plantilla a modificar")
            inumeroCama=int(input())
            data=servicio.modificaPlantilla(inumeroPlantilla, inombrePlantilla, idireccion, itelefono, inumeroCama)
            print(f"afectados:{data}")
            return data
        
        def BuscarOracleDePlantilla():
            servicio = service.ServiceOraclePlantilla()
            print("dame un numero para el departamento a buscar")
            deptno=int(input())
            afectados=servicio.buscarOraclePlantilla(deptno)
            print(f"Departamento encontrado: {deptno}, {afectados}")
            return afectados
