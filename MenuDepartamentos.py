from services import servicio04OracleDepartamento as service
from models import departamento 

class MENUDEPARTAMENTO:
    def nuevoDepartamento():
        servicio = service.ServiceOracleDepartamentos()
        print("dame un numero para el departamento nuevo")
        deptno=int(input())
        print("dame un nombre para el departamento nuevo")
        dname=input()
        print("dame una localizacion para el departamento nuevo" )
        LOCA=input()
        afectados=servicio.insertarDepartamento(deptno, dname, LOCA)
        print(f"Departamento insertado: {afectados}")


    def BuscarOracleDepartamentoID():
        servicio = service.ServiceOracleDepartamentos()
        print("dame un numero para el departamento a buscar")
        deptno=int(input())
        afectados=servicio.buscarDepartamentoNumero(deptno)
        print(f"Departamento encontrado: {deptno}, {afectados}")
        return afectados

    def borrarDepartamentoNumero():
        servicio=service.ServiceOracleDepartamentos()
        print("dame un numero para el departamento a Borrar")
        numero=int(input())
        afectados=servicio.borrarDepartamentoNumero(numero)
        print(f"Departamento eliminado numero {numero}: ,afectado: {afectados}")

    def modificarDepartamentoNumero():
        servicio=service.ServiceOracleDepartamentos()
        print("dame un numero para el departamento a modificar")
        numero=int(input())
        print("dame un nombre para el departamento a modificar")
        nombre=input()
        print("dame una localidad para el departamento a modificar")
        localidad=input()
        afectados=servicio.modificarDepartamento(numero, nombre, localidad )
        print(f"Departamento modificado numero {numero}: ,afectado: {afectados}")

    def mostrarDepartamentos():
        servicio=service.ServiceOracleDepartamentos()
        afectados=servicio.mostrarDepartamento()
        for fila in afectados:
            print( fila.numero, fila.nombre , fila.localidad)
