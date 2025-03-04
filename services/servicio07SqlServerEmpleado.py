import pyodbc
from models.empleado import Empleado



class ServiceSqlServerEmpleado:

    def __init__(self):
        conection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
        if conection:
            print(f".....conexion correcta {conection}")
        else:
            print("fallo de conexion")

    def muestraEmpleado(self):
        sql="""select * 
                from EMP """
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            emp=ServiceSqlServerEmpleado()
            emp.idEmpleado=row[0]
            emp.apellido=row[1]
            emp.oficio=row[2]
            emp.salario=row[5]
            datos.append(row)
        cursor.close()
        return datos

    def muestraEmpleadoSalario(self):
        sql="""select * 
                from EMP where SALARIO >= ? """
        cursor = self.conexion.cursor()
        cursor.execute(sql, (SALARIO, ))
        datos = []
        for row in cursor:
            emp=Empleado()
            emp.idEmpleado=row[0]
            emp.apellido=row[1]
            emp.oficio=row[2]
            emp.salario=row[5]
            datos.append(row)
        cursor.close()
        return datos

    def insertarEmpleado(self,Empleado_cod , nombre , direccion , telefono , num_cama):
        sql="insert into Empleado values(:Empleado_cod , :nombre , :direccion , :telefono , :num_cama)"
        cursor=self.conexion.cursor()
        cursor.execute(sql, (Empleado_cod , nombre , direccion , telefono , num_cama))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarEmpleado(self, idEmpleado):
        sql="delete from Empleado where Empleado_cod=:idEmpleado"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (idEmpleado, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaEmpleado(self, Empleado_cod , nombre , direccion , telefono , num_cama):
        sql="""
                update Empleado 
                set nombre=':inombre',
                direccion=':idireccion',
                telefono=:itelefono , 
                num_cama=:inum_cama
                where Empleado_cod=:Empleado_cod
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( Empleado_cod , nombre , direccion , telefono , num_cama ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros


