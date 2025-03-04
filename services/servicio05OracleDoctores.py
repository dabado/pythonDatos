import oracledb
from models import doctor as model

class ServiceOracleDoctores:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraDoctores(self):
        sql="select * from doctor"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            modelo = model.Doctor()
            modelo.numeroHospital = row[0]
            modelo.numeroDoctor = row[1]
            modelo.apellido = row[2]
            modelo.especialidad = row[3]
            modelo.salario = row[4]
            datos.append(modelo)
        cursor.close()
        return datos

    def insertarDoctor(self,inumeroHospital,inumeroDoctor, iapellido, iespecialidad, isalario):
        sql="insert into DOCTOR values (:numeroHospital, :numeroDoctor, :apellido , :especialidad, :salario)"
        cursor = self.conexion.cursor()
        cursor.execute(sql, (inumeroHospital,inumeroDoctor, iapellido, iespecialidad, isalario))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print("Ho9laaaa")
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarDoctor(self, iddoctor):
        sql="delete from DOCTOR where doctor_no=:iddoctor"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (iddoctor, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaDoctor(self,inumeroHospital,inumeroDoctor, iapellido, iespecialidad, isalario):
        sql="update DOCTOR set( hospital_cod = :inumeroHospital , doctor_no = :inumeroDoctor, apellido = :iapellido,  especialidad = :iespecialidad, salario = :isalario) where doctor_no = :inumeroDoctor"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (inumeroHospital,inumeroDoctor, iapellido, iespecialidad, isalario))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros


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
            where DEPT_NO=:numero
            """
        cursor = self.conexion.cursor()
        cursor.execute(sql, (numero, ))
        registros = cursor.rowcount

        self.conexion.commit()
        cursor.close()
        return registros
    
    def modificarDepartamentoNumero(self, numero, nombre , localidad):
        sql= "UPDATE DEPT set (DNOMBRE=:nombre,loc=:localizacion where DEPT_NO=:numero )"
        
        cursor = self.conexion.cursor()
        cursor.execute(sql, (numero, nombre ,localidad ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return registros


    def mostrarDepartamento(self):
        sql="select * from DEPT"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            modelo = departamento.departamento()
            modelo.numero = row[0]
            modelo.nombre = row[1]
            modelo.localidad = row[2]
            datos.append(modelo)
        cursor.close()
        return datos