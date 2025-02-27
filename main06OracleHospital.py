from services import servicio06OracleHospital as service
from models import hospital

def mostrarHospitales():
    servicio=service.ServiceOracleHospital()
    afectados=servicio.muestraHospital()
    for fila in afectados:
        print(fila.numeroHospital, fila.numeroHospital, fila.apellido, fila.especialidad, fila.salario)


def nuevoHospital():
    servicio=service.ServiceOracleHospital()
    #afectados=servicio.insertarHospital(numeroHospital,numeroHospital, apellido, especialidad, salario)
    print("dame un numeroHospital para el Hospital nuevo")
    inumeroHospital=int(input())
    print("dame un numeroHospital para el Hospital nuevo")
    inumeroHospital=int(input())
    print("dame una apellido para el departamento nuevo" )
    iapellido=input()
    print("dame una especialidad para el departamento nuevo" )
    iespecialidad=input()
    print("dame una salario para el departamento nuevo" )
    isalario=int(input())
    data=servicio.insertarHospital(inumeroHospital,inumeroHospital, iapellido, iespecialidad, isalario)
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
    print("dame un numero para el inumeroHospital a modificar")
    inumeroHospital=int(input())
    print("dame un  iapellido a modificar")
    iapellido=input()
    print("dame una especialidad para la iespecialidad a modificar")
    iespecialidad=input()
    print("dame un numero para el isalario a modificar")
    isalario=int(input())
    data=servicio.modificaHospital(inumeroHospital,inumeroHospital, iapellido, iespecialidad, isalario)
    print(f"afectados:{data}")
    return data




def menu():
    servicio=service.ServiceOracleHospital()
    print("1._Insertar departamento")
    print("2._Buscar departamento")
    print("3._borrar Departamento por Numero")
    print("4._modificar Departamento por Numero")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        mostrarHospitales()
    elif (opcion == 2):
        resultado=nuevoHospital()
        print(resultado)
    elif (opcion == 3):
        resultado=quitarHospital()
        print(resultado)
    elif (opcion == 4):
        resultado=modificarHospital()
        print(resultado)
    else:
        print("introcuce un dato valido")
#nuevoDepartamento()
#nuevoHospital()
menu()