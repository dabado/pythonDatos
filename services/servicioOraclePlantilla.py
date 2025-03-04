import oracledb
from models import plantilla 


class ServiceOraclePlantilla:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraPlantilla(self):
        sql="""select *
                 from Plantilla"""
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            
            datos.append(row)

        cursor.close()
        return datos

    def insertarPlantilla(self, hospital_cod,  sala_cod, empleado_no, apellido, funcion, turno, salario):
        sql="""insert into Plantilla
                 values (:hospital_cod ,
                   :sala_cod , 
                   :empleado_no , 
                   :apellido , 
                   :funcion , 
                   :turno , 
                   :salario) """
        cursor=self.conexion.cursor()
        cursor.execute(sql, ( hospital_cod,  sala_cod, empleado_no, apellido,    funcion,  turno,   salario))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarPlantilla(self, empleado_no):
        sql="""delete from Plantilla 
                where empleado_no=:empleado_no """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (empleado_no, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaPlantilla(self, hospital_cod,  sala_cod, empleado_no, apellido,  funcion,  turno,   salario):
        sql="""
                update Plantilla 
                set hospital_cod=':hospital_cod',
                sala_cod=':sala_cod',
                apellido=:apellido ,
                funcion=:funcion ,
                turno=:turno ,
                salario=:salario
                where empleado_no=:empleado_no
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( hospital_cod,  sala_cod, empleado_no, apellido,    funcion,  turno,   salario ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros


    def buscarPlantillaNumero(self):

        sql = "select * from DEPT where DEPT_NO=:DEPT_NO" 
        cursor=self.conexion.cursor()
        cursor.execute(sql, (DEPT_NO, ))
                #COMO ESTAMOS BUSCANDO POR PK, SOLAMENTE NOS PUEDE 
                #DEVOLVER UNA FILA
        row = cursor.fetchone()
                #DEBEMOS COMPROBAR SI FILA TIENE CONTENIDO/ALGO
        if (not row):
            print("No existe el departamento")
        else:
                    #DIBUJAMOS LOS DATOS
            nombre = row[1]
            localidad = row[2]
            print(nombre + ", " + localidad)
        cursor.close()
        
        print("Fin de bbdd")