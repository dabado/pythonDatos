import oracledb
import mysql.connector as bd
from models import hospital 
# Hospital_cod , nombre , direccion , telefono , num_cama


class ServiceOracleHospital:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraHospitales(self):
        sql="select * from Hospital"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            
            datos.append(row)
            """
            modelo = model.Hospital()
            modelo.Hospital_cod = row[0]
            modelo.nombre = row[1]
            modelo.direccion = row[2]
            modelo.telefono = row[3]
            modelo.num_cama = row[4]
            datos.append(modelo)
            """
        cursor.close()
        return datos

    def insertarHospital(self,Hospital_cod , nombre , direccion , telefono , num_cama):
        sql="insert into Hospital values(:Hospital_cod , :nombre , :direccion , :telefono , :num_cama)"
        cursor=self.conexion.cursor()
        cursor.execute(sql, (Hospital_cod , nombre , direccion , telefono , num_cama))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarHospital(self, idHospital):
        sql="delete from Hospital where Hospital_cod=:idHospital"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (idHospital, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaHospital(self, Hospital_cod , nombre , direccion , telefono , num_cama):
        sql="""
                update Hospital 
                set nombre=':inombre',
                direccion=':idireccion',
                telefono=:itelefono , 
                num_cama=:inum_cama
                where Hospital_cod=:Hospital_cod
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( Hospital_cod , nombre , direccion , telefono , num_cama ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros



