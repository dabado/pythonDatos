from services import servicio06OracleHospital as service
from models import hospital

def mostrarHospitales():
    servicio=service.ServiceOracleHospital()
    afectados=servicio.muestraHospitales()
    
    for fila in afectados:
        print(fila)
        #print(fila.numeroHospital, fila.numeroHospital, fila.apellido, fila.especialidad, fila.salario)


def nuevoHospital():
    servicio=service.ServiceOracleHospital()
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
    numeroHospital=int(input())
    print(f"dame un inombreHospital para el {numeroHospital} a modificar")
    nombreHospital=input()
    print("dame una idireccion a modificar")
    direccion=input()
    print("dame un telefono el Hospital a modificar")
    telefono=int(input())
    print("dame un numero de camas para el Hospital a modificar")
    numeroCama=int(input())

    data=servicio.modificaHospital(numeroHospital , nombreHospital , direccion , telefono , numeroCama)
    print(f"afectados:{data}")
    return data




def menuHospital():
    servicio=service.ServiceOracleHospital()

    while True:
        print("1.Mostrar Hospital")
        print("2.nuevo Hospital")
        print("3._borrar Hospital por Numero")
        print("4._modificar Hospital por Numero")
        print("0._volver al menu principal")
        print("elije accion")
        #opcion = input("Seleccione una opción: ")
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
        elif (opcion == 0):
            break
        else:
            
            print("introcuce un dato valido")

def menu():
    servicio=service.ServiceOracleHospital()

    while True:
        print("1.Mostrar menu Hospital")
        print("2.nuevo")
        print("3._borrar  por Numero")
        print("4._modificar  por Numero")
        print("0.Mostrar menu Hospital")
        print("elije accion")
        #opcion = input("Seleccione una opción: ")
        opcion=int(input())
        
        if (opcion == 1):
            menuHospital()
        elif (opcion == 2):
            resultado=nuevoHospital()
            print(resultado)
        elif (opcion == 3):
            resultado=quitarHospital()
            print(resultado)
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


menu()
