#from services import servicioOracleEnfermo as service

from models import hospital
from models import doctor
from models import departamento
from models import plantilla
from models import empleado
from models import sala
from models import enfermo

from MenuHospital import MENUHOSPITAL
from MenuDoctores import MENUDOCTORES
from MenuDepartamentos import MENUDEPARTAMENTO
from MenuPlantilla import MENUPLANTILLA
from MenuEmpleado import MENUEMPLEADO
from MenuEnfermo import MENUDENFERMO
from MenuSala import MENUSALA



def menuEnfermo():
    while True:
        print("1.Mostrar Enfermo")
        print("2.nuevo Enfermo")
        print("3._borrar Enfermo por Numero")
        print("4._modificar Enfermo por Numero")
        print("0._volver al menu principal")
        print("elije accion")
        opcion=int(input())
        
        if (opcion == 1):
            MENUDENFERMO.mostrarEnfermos()
        elif (opcion == 2):
           MENUDENFERMO.nuevoEnfermo()
        elif (opcion == 3):
            MENUDENFERMO.borrarEnfermoNumero
        elif (opcion == 4):
            MENUDENFERMO.modificarEnfermoNumero
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


def menuEmpleado():
    while True:
        print("1.Mostrar Empleado")
        print("2.nuevo Empleado")
        print("3._borrar Empleado por Numero")
        print("4._modificar Empleado por Numero")
        print("0._volver al menu principal")
        print("elije accion")
        opcion=int(input())
        if (opcion == 1):
            MENUEMPLEADO.mostrarEmpleado()
        elif (opcion == 2):
           MENUEMPLEADO.nuevoEmpleado()
        elif (opcion == 3):
            MENUEMPLEADO.borrarEmpleadoNumero
        elif (opcion == 4):
            MENUEMPLEADO.modificarEmpleadoNumero
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


def menuSala():
    while True:
        print("1.Mostrar Sala")
        print("2.nuevo Sala")
        print("3._borrar Sala por Numero")
        print("4._modificar Sala por Numero")
        print("0._volver al menu principal")
        print("elije accion")
        opcion=int(input())
        if (opcion == 1):
            MENUSALA.mostrarsala()
        elif (opcion == 2):
           MENUSALA.nuevosala()
        elif (opcion == 3):
            MENUSALA.quitarsala
        elif (opcion == 4):
            MENUSALA.modificarsala
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")



def menuPlantilla():
    print("1.mostrar Plantilla")
    print("2._Buscar Plantilla")
    print("3._borrar Plantilla por Numero")
    print("4._modificar Plantilla por Numero")
    print("5.nueva Plantilla")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        MENUPLANTILLA.muestraPlantilla()
    elif (opcion == 2):
        MENUPLANTILLA.BuscarPlantilla()
    elif (opcion == 3):
        MENUPLANTILLA.quitarPlantilla()
    elif (opcion == 4):
        MENUPLANTILLA.modificarPlantilla()
    elif (opcion == 5):
        MENUPLANTILLA.nuevoPlantilla()
    else:
        print("introcuce un dato valido")


def menuDepartamento():
    print("1.Mostrar departamento")
    print("2._Buscar departamento")
    print("3._borrar Departamento por Numero")
    print("4._modificar Departamento por Numero")
    print("5.Nuevo Departamentos")
    print("elije accion")
    opcion=int(input())
    if (opcion == 1):
        MENUDEPARTAMENTO.mostrarDepartamentos()
    elif (opcion == 2):
        MENUDEPARTAMENTO.BuscarOracleDepartamentoID()
    elif (opcion == 3):
        MENUDEPARTAMENTO.borrarDepartamentoNumero()
    elif (opcion == 4):
        MENUDEPARTAMENTO.modificarDepartamentoNumero()
    elif (opcion == 5):
        MENUDEPARTAMENTO.nuevoDepartamento()
    else:
        print("introcuce un dato valido")

def menuDoctores():
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
    while True:
        print("1.Mostrar Hospital")
        print("2.nuevo Hospital")
        print("3._borrar Hospital por Numero")
        print("4._modificar Hospital por Numero")
        print("0._volver al menu principal")
        print("elije accion")
        opcion=int(input())
        if (opcion == 1):
            MENUHOSPITAL.mostrarHospitales()
        elif (opcion == 2):
           MENUHOSPITAL.nuevoHospital()
        elif (opcion == 3):
            MENUHOSPITAL.quitarHospital()
        elif (opcion == 4):
            MENUHOSPITAL.modificarHospital()
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")

def menu():
    while True:
        print("1.Mostrar menu Hospital")
        print("2.Mostrar menu Doctores")
        print("3.Mostrar menu Departamentod")
        print("4._Mostrar menu Empleado")
        print("5._Mostrar menu enfermo")
        print("6._Mostrar menu sala")
        print("7._Mostrar menu Plantilla")
        print("0.salir")
        print("elije accion")
        opcion=int(input())
        if (opcion == 1):
            menuHospital()
        elif (opcion == 2):
            menuDoctores()
        elif (opcion == 3):
            menuDepartamento()
        elif (opcion == 4):
            menuEmpleado()
        elif (opcion == 5):
            menuEnfermo()
        elif (opcion == 6):
            menuSala()
        elif (opcion == 7):
            menuPlantilla()
        elif (opcion == 0):
            break
        else:
            print("introcuce un dato valido")


menu()
