
from services import servicioOraclePlantilla as service
from models import plantilla 

class MENUPLANTILLA:
        #servicio=service.ServiceOraclePlantilla()
        def muestraPlantilla():
            servicio=service.ServiceOraclePlantilla()
            afectados=servicio.muestraPlantilla()
            for fila in afectados:
                print(fila)
                #print(fila.numeroPlantilla, fila.numeroPlantilla, fila.apellido, fila.especialidad, fila.salario)


        def nuevoPlantilla():
            servicio=service.ServiceOraclePlantilla()
            #afectados=servicio.insertarPlantilla(numeroPlantilla,nombrePlantilla, direccion, telefono, numeroCama)
            print("dame un codigo de Hospital para el Plantilla nuevo")
            hospital_cod=int(input())
            print("dame una sala para el  nuevo" )
            sala_cod=int(input())
            print("dame un numero de empleado  para el  nuevo" )
            empleado_no=int(input())
            print("dame un apellido para el  nuevo" )
            apellido=input()   
            print("dame una funcion para el  nuevo" )
            funcion=input()
            print("dame un turno para el  nuevo" )
            turno=input()
            print("dame un salario para el  nuevo" )
            salario=int(input())
            data=servicio.insertarPlantilla(hospital_cod,  sala_cod, empleado_no, apellido,  funcion,  turno,   salario)

            print(f"nuevo {data}")
            return data

        def quitarPlantilla():
            servicio=service.ServiceOraclePlantilla()
            print("dame un empleado_no para el Plantilla a eliminar")
            empleado_no=int(input())
            data=servicio.eliminarPlantilla( empleado_no )
            
            print(f"afectados: {data}")
            return data

        def modificarPlantilla():
            servicio=service.ServiceOraclePlantilla()
            print("dame un numero para el Hospital a modificar")
            hospital_cod=int(input())
            print("dame un sala para el  a modificar")
            sala_cod=input()
            print("dame un  numero empleado a modificar")
            empleado_no=input()
            print("dame un apellido  a modificar")
            apellido=int(input())
            print("dame una funcion  para el empleado a modificar")
            funcion=int(input())
            print("dame un turno para el enpleado a modificar")
            turno=int(input())
            print("dame un salaro para el enpleado a modificar")
            salario=int(input())
            data=servicio.modificaPlantilla(hospital_cod,  sala_cod, empleado_no, apellido,  funcion,  turno,   salario)
            print(f"afectados:{data}")
            return data
        
        def buscarPlantilla():
            servicio = service.ServiceOraclePlantilla()
            print("dame un numero para el departamento a buscar")
            hospital_cod=int(input())
            afectados=servicio.buscarOraclePlantilla(hospital_cod)
            print(f"Departamento encontrado: {hospital_cod}, {afectados}")
            return afectados



        def buscarPlantillaNumero():
                print("Introduzca número de departamento")
                data = input()
                cursor = self.conection.cursor()

                
        def buscadorPlantillaHospital():
                print("Introduzca un Turno (T, M, N)")
                data = input()
                sql = "select APELLIDO, FUNCION from PLANTILLA where hospital_cod=" + data 
                print(sql)
                connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
                cursor = connection.cursor()
                cursor.execute(sql)
                #RECORREMOS LOS DATOS DEL CURSOR
                for apellido, funcion in cursor:
                    print(apellido + ", Función: " + funcion)
                cursor.close()
                connection.close()
                print("Fin de BBDD")

        def buscarPlantillaTurno():
                sqlturnos = """
                    select distinct TURNO, case TURNO 
                    when 'T' then 'TARDE' 
                    when 'M' then 'MAÑANA' 
                    else 'NOCHE' 
                    end as VALOR
                    from PLANTILLA
                """
                cursor = connection.cursor()
                cursor.execute(sqlturnos)
                listaTurnos = []
                contador = 1
                for row in cursor:
                    listaTurnos.append(row[0])
                    print(f"{contador} .- {row[1]}")
                    contador += 1
                cursor.close()
                print("Seleccione una opción")
                opcion = int(input()) - 1
                turno = listaTurnos[opcion]
                sqlplantilla = "select * from PLANTILLA where TURNO=:p1"
                cursor = connection.cursor()
                cursor.execute(sqlplantilla, (turno,))
                for row in cursor:
                    print(row)
                cursor.close()
                connection.close()
                print("Fin de programa")
