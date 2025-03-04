
from services import servicioOracleSala as service
from models import sala

class MENUSALA:
        servicio=service.ServiceOracleSala()
        def mostrarsala():
            servicio=service.ServiceOracleSala()
            afectados=servicio.muestraSala()
            for fila in afectados:
                print(fila)
                #print(fila.numerosala, fila.numerosala, fila.apellido, fila.especialidad, fila.salario)


        def nuevosala():
            servicio=service.ServiceOraclesala()
            #afectados=servicio.insertarsala(numerosala,nombresala, direccion, telefono, numeroCama)
            print("dame un numerosala para el sala nuevo")
            inumerosala=int(input())
            print("dame una nombresala para el sala nuevo" )
            inombresala=input()
            print("dame una direccion para el sala nuevo" )
            idireccion=input()
            print("dame un numeroCama para el sala nuevo" )
            inumeroCama=int(input())     
            print("dame un telefono para el sala nuevo" )
            itelefono=int(input())

            data=servicio.insertarsala(inumerosala,inombresala, idireccion, itelefono, inumeroCama)

            print(f"nuevo {data}")
            return data

        def quitarsala():
            servicio=service.ServiceOracleSala()
            print("dame un numerosala para el sala a eliminar")
            inumerosala=int(input())
            data=servicio.eliminarsala(inumerosala)
            
            print(f"afectados: {data}")
            return data

        def modificarsala():
            servicio=service.ServiceOraclesala()
            print("dame un numero para el inumerosala a modificar")
            inumerosala=int(input())
            print("dame un inombresala para el {inumerosala} a modificar")
            inombresala=input()
            print("dame un  idireccion a modificar")
            idireccion=input()
            print("dame un telefono el sala a modificar")
            itelefono=int(input())
            print("dame un numero de camas para el sala a modificar")
            inumeroCama=int(input())
            data=servicio.modificasala(inumerosala, inombresala, idireccion, itelefono, inumeroCama)
            print(f"afectados:{data}")
            return data

