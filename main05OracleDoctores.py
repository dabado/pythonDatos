from services import servicio04OracleDepartamento as service
from services import servicio05OracleDoctores
from models import departamento 
from models import doctor

def mostrarDoctores():
    servicio=servicio05OracleDoctores.ServiceOracleDoctores()
    afectados=servicio.muestraDoctores()
    for fila in afectados:
        print(fila.numeroHospital, fila.numeroDoctor, fila.apellido, fila.especialidad, fila.salario)


def nuevoDoctor():
    servicio=servicio05OracleDoctores.ServiceOracleDoctores()
    #afectados=servicio.insertarDoctor(numeroHospital,numeroDoctor, apellido, especialidad, salario)
    print("dame un numeroHospital para el doctor nuevo")
    inumeroHospital=int(input())
    print("dame un numeroDoctor para el doctor nuevo")
    inumeroDoctor=int(input())
    print("dame una apellido para el departamento nuevo" )
    iapellido=input()
    print("dame una especialidad para el departamento nuevo" )
    iespecialidad=input()
    print("dame una salario para el departamento nuevo" )
    isalario=int(input())
    data=servicio.insertarDoctor(inumeroHospital,inumeroDoctor, iapellido, iespecialidad, isalario)
    print(f"nuevo {data}")
    return data

def quitarDoctor():
    servicio=servicio05OracleDoctores.ServiceOracleDoctores()
    print("dame un numeroDoctor para el doctor a eliminar")
    inumeroDoctor=int(input())
    data=servicio.eliminarDoctor(inumeroDoctor)
    print(f"afectados: {data}")
    return data

def modificarDoctor():
    servicio=servicio05OracleDoctores.ServiceOracleDoctores()
    print("dame un numero para el inumeroHospital a modificar")
    inumeroHospital=int(input())
    print("dame un numero para el inumeroDoctor a modificar")
    inumeroDoctor=int(input())
    print("dame un numero para el iapellido a modificar")
    iapellido=int(input())
    print("dame un numero para la iespecialidad a modificar")
    iespecialidad=int(input())
    print("dame un numero para el isalario a modificar")
    isalario=int(input())
    data=servicio.modificaDoctor(inumeroHospital,inumeroDoctor, iapellido, iespecialidad, isalario)
    print(f"afectados:{data}")
    return data


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

def menu():
    servicio = service.ServiceOracleDepartamentos()
    print("1._Insertar departamento")
    print("2._Buscar departamento")
    print("3._borrar Departamento por Numero")
    print("4._modificar Departamento por Numero")
    print("5._mostrar Departamentos")
    print("6._mostrar doctores")
    print("7._nuevo doctor ")
    print("8._eliminar doctor ")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        nuevoDepartamento()
    elif (opcion == 2):
        #dept = servicio.buscarDepartamentoNumero()
        BuscarOracleDepartamentoID()
    elif (opcion == 3):
        borrarDepartamentoNumero()
    elif (opcion == 4):
        modificarDepartamentoNumero()
    elif (opcion == 5):
        mostrarDepartamentos()
    elif (opcion == 6):
        mostrarDoctores()
    elif (opcion == 7):
        resultado=nuevoDoctor()
        print(resultado)
    elif (opcion == 8):
        resultado=quitarDoctor()
        print(resultado)
    elif (opcion == 9):
        resultado=modificarDoctor()
    else:
        print("introcuce un dato valido")
#nuevoDepartamento()
#nuevoDoctor()
menu()