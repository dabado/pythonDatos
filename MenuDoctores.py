from services import servicio05OracleDoctores
from models import doctor

class MENUDOCTORES:

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
