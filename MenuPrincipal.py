#from services import servicio06OracleHospital as service
from models import hospital
from MenuHospital import MENUHOSPITAL
from MenuDoctores import MENUDOCTORES


def menuDoctores():
    #servicio = service.ServiceOracleDepartamentos()
    while True:
        print("1._mostrar doctores")
        print("2._Nuevo doctor ")
        print("3._Modificar doctor ")
        print("4._Eliminar doctor ")
        print("0._volver al menu principal")
        print("elije accion")
        opcion=int(input())
        if (opcion == 1):
            MENUDOCTORES.mostrarDoctores()
        elif (opcion == 2):
            MENUDOCTORES.nuevoDoctor()
        elif (opcion == 3):
            MENUDOCTORES.modificarDoctor()
        elif (opcion == 4):
            MENUDOCTORES.quitarDoctor()
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


def menuHospital():
    #servicio=service.ServiceOracleHospital()

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
            MENUHOSPITAL.mostrarHospitales()
        elif (opcion == 2):
           MENUHOSPITAL.nuevoHospital()
        elif (opcion == 3):
            MENUHOSPITAL.quitarHospital
        elif (opcion == 4):
            MENUHOSPITAL.modificarHospital
        elif (opcion == 0):
            break
        else:
            
            print("introcuce un dato valido")

def menu():
    #servicio=service.ServiceOracleHospital()

    while True:
        print("1.Mostrar menu Hospital")
        print("2.Mostrar menu Doctores")
        print("3._borrar  por Numero")
        print("4._modificar  por Numero")
        print("0.Mostrar menu Hospital")
        print("elije accion")
        #opcion = input("Seleccione una opción: ")
        opcion=int(input())
        
        if (opcion == 1):
            menuHospital()
        elif (opcion == 2):
            menuDoctores()
        elif (opcion == 3):
            menuTurnos()
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


menu()