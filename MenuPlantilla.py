
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
            print("dame un codigo de Hospital para el Plantilla nuevo")
            hospital_cod=int(input())
            print("dame una sala para el  nuevo" )
            sala_cod=int(input())
            print("dame un numero de empleado  para el  nuevo" )
            empleado_no=int(input())
            print("dame un apellido para el  nuevo" )
            apellido=input()   
            print("dame una funcion para el  nuevo" )
            funcion=input()
            print("dame un turno para el  nuevo" )
            turno=input()
            print("dame un salario para el  nuevo" )
            salario=int(input())
            data=servicio.insertarPlantilla(hospital_cod,  sala_cod, empleado_no, apellido,  funcion,  turno,   salario)

            print(f"nuevo {data}")
            return data

        def quitarPlantilla():
            servicio=service.ServiceOraclePlantilla()
            print("dame un empleado_no para el Plantilla a eliminar")
            empleado_no=int(input())
            data=servicio.eliminarPlantilla( empleado_no )
            
            print(f"afectados: {data}")
            return data

        def modificarPlantilla():
            servicio=service.ServiceOraclePlantilla()
            print("dame un numero para el Hospital a modificar")
            hospital_cod=int(input())
            print("dame un sala para el  a modificar")
            sala_cod=input()
            print("dame un  numero empleado a modificar")
            empleado_no=input()
            print("dame un apellido  a modificar")
            apellido=int(input())
            print("dame una funcion  para el empleado a modificar")
            funcion=int(input())
            print("dame un turno para el enpleado a modificar")
            turno=int(input())
            data=servicio.modificaPlantilla(hospital_cod,  sala_cod, empleado_no, apellido,  funcion,  turno,   salario)
            print(f"afectados:{data}")
            return data
        
        def BuscarOracleDePlantilla():
            servicio = service.ServiceOraclePlantilla()
            print("dame un numero para el departamento a buscar")
            hospital_cod=int(input())
            afectados=servicio.buscarOraclePlantilla(hospital_cod)
            print(f"Departamento encontrado: {hospital_cod}, {afectados}")
            return afectados
