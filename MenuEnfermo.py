
from services import servicioOracleEnfermo as service
from models import enfermo 

class MENUDENFERMO:
    servicio = service.ServiceOracleEnfermo()
    def nuevoEnfermo():
        #servicio = service.ServiceOracleEnfermo()
        print("dame un numero para el Enfermo nuevo")
        inscripcion=int(input())
        print("dame un nombre para el Enfermo nuevo")
        apellido=input()
        print("dame una localizacion para el Enfermo nuevo" )
        direccion=input()
        print("dame una fecha de nacimiento para el Enfermo nuevo" )
        fecha_nac=input()
        print("dame un sexo para el Enfermo nuevo" )
        sexo=input()
        print("dame un numero de seguridad social para el Enfermo nuevo" )
        nss=input()
        afectados=service.ServiceOracleEnfermo(inscripcion , apellido , direccion, fecha_nac, sexo, nss)
        print(f"Enfermo insertado: {afectados}")


    def BuscarOracleEnfermoID():
        servicio = service.ServiceOracleEnfermo()
        print("dame un numero para el Enfermo a buscar")
        deptno=int(input())
        afectados=servicio.buscarEnfermoNumero(deptno)
        print(f"Enfermo encontrado: {deptno}, {afectados}")
        return afectados

    def borrarEnfermoNumero():
        servicio=service.ServiceOracleEnfermo()
        print("dame un numero para el Enfermo a Borrar")
        numero=int(input())
        afectados=servicio.eliminarEnfermo(numero)
        print(f"Enfermo eliminado numero {numero}: ,afectado: {afectados}")

    def modificarEnfermoNumero():
        servicio=service.ServiceOracleEnfermo()
        print("dame un numero para el Enfermo a modificar")
        numero=int(input())
        print("dame un nombre para el Enfermo a modificar")
        nombre=input()
        print("dame una localidad para el Enfermo a modificar")
        localidad=input()
        afectados=servicio.modificaEnfermo(inscripcion , apellido , direccion, fecha_nac, sexo, nss)
        print(f"Enfermo modificado numero {numero}: ,afectado: {afectados}")

    def mostrarEnfermos():
        servicio=service.ServiceOracleEnfermo()
        afectados=servicio.muestraEnfermo()
        for fila in afectados:
            print( fila)
