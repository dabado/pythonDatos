import oracledb
from models import empleado 
# Empleado_cod , nombre , direccion , telefono , num_cama


class ServiceOracleEmpleado:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraEmpleado(self):
        sql="select * from EMP"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            datos.append(row)
        cursor.close()
        self.conexion.close()
        return datos

    def insertarEmpleado(self, emp_no, apellido , oficio , dir , fecha_alta , salario, comision, dept_no):
        sql="insert into EMP values(  :apellido , :oficio , :dir , :fecha_alta , :salario, :comision, :dept_no) where emp_no=:emp_no"
        cursor=self.conexion.cursor()
        cursor.execute(sql, ( emp_no, apellido , oficio , dir , fecha_alta , salario, comision, dept_no ))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        self.conexion.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarEmpleado(self, idEmpleado):
        sql="delete from EMP where emp_cod=:emp_cod"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (emp_cod , ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        self.conexion.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaEmpleado(self, emp_no, apellido , oficio , dir , fecha_alta , salario, comision, dept_no):
        sql="""
                update Empleado 
                set emp_no=':emp_no',
                apellido=':apellido',
                oficio=:oficio , 
                dir=:dir,
                fecha_alta=:fecha_alta,
                salario=:salario,
                comision=:comision
                where dept_no=:dept_no
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( emp_no, apellido , oficio , dir , fecha_alta , salario, comision, dept_no ))
        registros=cursor.rowcount
        self.conexion.commit()
        
        print(f"modificados: {registros} registros")
        cursor.close()
        self.conexion.close()
        return registros



