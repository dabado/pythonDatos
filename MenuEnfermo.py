
from services import servicioOracleEnfermo as service
from models import enfermo 

class MENUDENFERMO:
    servicio = service.ServiceOracleEnfermo()
    def nuevoEnfermo():
        servicio = service.ServiceOracleEnfermo()
        print("dame un numero para el Enfermo nuevo")
        deptno=int(input())
        print("dame un nombre para el Enfermo nuevo")
        dname=input()
        print("dame una localizacion para el Enfermo nuevo" )
        LOCA=input()
        afectados=servicio.insertarSala(deptno, dname, LOCA)
        print(f"Enfermo insertado: {afectados}")


    def BuscarOracleEnfermoID():
        servicio = service.ServiceOracleEnfermos()
        print("dame un numero para el Enfermo a buscar")
        deptno=int(input())
        afectados=servicio.buscarEnfermoNumero(deptno)
        print(f"Enfermo encontrado: {deptno}, {afectados}")
        return afectados

    def borrarEnfermoNumero():
        servicio=service.ServiceOracleEnfermos()
        print("dame un numero para el Enfermo a Borrar")
        numero=int(input())
        afectados=servicio.borrarEnfermoNumero(numero)
        print(f"Enfermo eliminado numero {numero}: ,afectado: {afectados}")

    def modificarEnfermoNumero():
        servicio=service.ServiceOracleEnfermos()
        print("dame un numero para el Enfermo a modificar")
        numero=int(input())
        print("dame un nombre para el Enfermo a modificar")
        nombre=input()
        print("dame una localidad para el Enfermo a modificar")
        localidad=input()
        afectados=servicio.modificarEnfermo(numero, nombre, localidad )
        print(f"Enfermo modificado numero {numero}: ,afectado: {afectados}")

    def mostrarEnfermos():
        servicio=service.ServiceOracleEnfermo()
        afectados=servicio.muestraEnfermo()
        for fila in afectados:
            print( fila)
