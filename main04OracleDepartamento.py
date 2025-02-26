from services import servicio04OracleDepartamento as service
from models import departamento 


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
    servicio = service.ServiceOracleDepartamentos()
    print("dame un numero para el departamento a Borrar")
    deptno=int(input())
    afectados=servicio.borrarDepartamentoNumero(deptno)
    print(f"Departamento encontrado: {deptno}, {afectados}")

def menu():
    servicio = service.ServiceOracleDepartamentos()
    print("1._Insertar departamento")
    print("2._Buscar departamento")
    print("3._borrar Departamento por Numero")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        nuevoDepartamento()
    elif (opcion == 2):
        #dept = servicio.buscarDepartamentoNumero()
        BuscarOracleDepartamentoID()
    elif (opcion == 3):
        borrarDepartamentoNumero()
    else:
        print("introcuce un dato valido")
#nuevoDepartamento()
menu()