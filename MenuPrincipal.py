from services import servicio06OracleHospital as service
from models import hospital
from models import doctor
from models import departamento
from models import plantilla

from MenuHospital import MENUHOSPITAL
from MenuDoctores import MENUDOCTORES
from MenuDepartamentos import MENUDEPARTAMENTO
from MenuPlantilla import MENUPLANTILLA

def menuPlantilla():
    #servicio = service.ServiceOraclePlantilla()
    print("1._Insertar Plantilla")
    print("2._Buscar Plantilla")
    print("3._borrar Plantilla por Numero")
    print("4._modificar Plantilla por Numero")
    print("5._mostrar Plantilla")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        MENUPLANTILLA.nuevoPlantilla()
    elif (opcion == 2):
        #dept = servicio.buscarDepartamentoNumero()
        MENUPLANTILLA.BuscarOraclePlantilla()
    elif (opcion == 3):
        MENUPLANTILLA.borrarPlantillaNumero()
    elif (opcion == 4):
        MENUPLANTILLA.modificarPlantillaNumero()
    elif (opcion == 5):
        MENUPLANTILLA.mostrarPlantilla()
    else:
        print("introcuce un dato valido")


def menuDepartamento():
    #servicio = service.ServiceOracleDepartamentos()
    print("1._Insertar departamento")
    print("2._Buscar departamento")
    print("3._borrar Departamento por Numero")
    print("4._modificar Departamento por Numero")
    print("5._mostrar Departamentos")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        MENUDEPARTAMENTO.nuevoDepartamento()
    elif (opcion == 2):
        #dept = servicio.buscarDepartamentoNumero()
        MENUDEPARTAMENTO.BuscarOracleDepartamentoID()
    elif (opcion == 3):
        MENUDEPARTAMENTO.borrarDepartamentoNumero()
    elif (opcion == 4):
        MENUDEPARTAMENTO.modificarDepartamentoNumero()
    elif (opcion == 5):
        MENUDEPARTAMENTO.mostrarDepartamentos()
    else:
        print("introcuce un dato valido")

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
        print("3.Mostrar menu Departamentod")
        print("4._Mostrar menu Plantilla")
        print("0.salir")
        print("elije accion")
        #opcion = input("Seleccione una opción: ")
        opcion=int(input())
        
        if (opcion == 1):
            menuHospital()
        elif (opcion == 2):
            menuDoctores()
        elif (opcion == 3):
            menuDepartamento()
        elif (opcion == 4):
            menuPlantilla()
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


menu()
