import oracledb
from models import sala 
# Enfermo_cod , nombre , direccion , telefono , num_cama


class ServiceOracleEnfermo:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraEnfermo(self):
        sql="select * from Enfermo"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            datos.append(row)
        cursor.close()
        return datos

    def insertarEnfermo(self,Enfermo_cod , nombre , direccion , telefono , num_cama):
        sql="insert into Enfermo values(:Enfermo_cod , :nombre , :direccion , :telefono , :num_cama)"
        cursor=self.conexion.cursor()
        cursor.execute(sql, (Enfermo_cod , nombre , direccion , telefono , num_cama))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarEnfermo(self, idEnfermo):
        sql="delete from Enfermo where Enfermo_cod=:idEnfermo"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (idEnfermo, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaEnfermo(self, Enfermo_cod , nombre , direccion , telefono , num_cama):
        sql="""
                update Enfermo 
                set nombre=':inombre',
                direccion=':idireccion',
                telefono=:itelefono , 
                num_cama=:inum_cama
                where Enfermo_cod=:Enfermo_cod
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( Enfermo_cod , nombre , direccion , telefono , num_cama ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros



