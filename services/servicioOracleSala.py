import oracledb
from models import sala 
# Sala_cod , nombre , direccion , telefono , num_cama


class ServiceOracleSala:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraSala(self):
        sql="select * from Sala"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            datos.append(row)
        cursor.close()
        return datos

    def insertarSala(self,Sala_cod , nombre , direccion , telefono , num_cama):
        sql="insert into Sala values(:Sala_cod , :nombre , :direccion , :telefono , :num_cama)"
        cursor=self.conexion.cursor()
        cursor.execute(sql, (Sala_cod , nombre , direccion , telefono , num_cama))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarSala(self, idSala):
        sql="delete from Sala where Sala_cod=:idSala"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (idSala, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaSala(self, Sala_cod , nombre , direccion , telefono , num_cama):
        sql="""
                update Sala 
                set nombre=':inombre',
                direccion=':idireccion',
                telefono=:itelefono , 
                num_cama=:inum_cama
                where Sala_cod=:Sala_cod
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( Sala_cod , nombre , direccion , telefono , num_cama ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros



