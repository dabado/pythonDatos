import oracledb
from models import departamento

class ServiceOracleDepartamentos:
    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")

    def insertarDepartamento(self, numero, nombre , localidad):
        sql="""
            insert into DEPT
            values (:id, :nombre , :localidad)
            """
        cursor = self.conexion.cursor()
        cursor.execute(sql, (numero, nombre , localidad ))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()

        cursor.close()
        return registrosAfectados

    def buscarDepartamentoNumero(self, numero):
        sql="""
            select *
            from DEPT
            where DEPT_NO = :p1
            """
        cursor = self.conexion.cursor()
        cursor.execute(sql, (numero, ))
        row = cursor.fetchone()
        modelo = departamento.departamento()
        modelo.numero = row[0]
        modelo.numero = row[1]
        modelo.numero = row[2]
        cursor.close()
        return modelo


    def borrarDepartamentoNumero(self, numero):
        sql="""
            DELETE FROM DEPT 
            where DEPT_NO = :p1
            """
        cursor = self.conexion.cursor()
        cursor.execute(sql, (numero, ))
        row = cursor.fetchone()
        modelo = departamento.departamento()
        modelo.numero = row[0]
        modelo.numero = row[1]
        modelo.numero = row[2]
        cursor.close()
        return modelo