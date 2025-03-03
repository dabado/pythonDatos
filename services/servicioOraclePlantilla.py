import oracledb
from models import plantilla 
# Plantilla_cod , nombre , direccion , telefono , num_cama


class ServiceOraclePlantilla:

    def __init__(self):
        self.conexion = oracledb.connect( user="system", password="oracle",dsn="localhost/xe")
        if self.conexion:
            print(f".....conexion correcta {self.conexion}")
        else:
            print("fallo de conexion")

    def muestraPlantilla(self):
        sql="select * from Plantilla"
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        datos = []
        for row in cursor:
            
            datos.append(row)
            """
        
            """
        cursor.close()
        return datos

    def insertarPlantilla(self,Plantilla_cod , nombre , direccion , telefono , num_cama):
        sql="insert into Plantilla values(:Plantilla_cod , :nombre , :direccion , :telefono , :num_cama)"
        cursor=self.conexion.cursor()
        cursor.execute(sql, (Plantilla_cod , nombre , direccion , telefono , num_cama))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"inse {registrosAfectados}")
        return registrosAfectados

    def eliminarPlantilla(self, idPlantilla):
        sql="delete from Plantilla where Plantilla_cod=:idPlantilla"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (idPlantilla, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaPlantilla(self, Plantilla_cod , nombre , direccion , telefono , num_cama):
        sql="""
                update Plantilla 
                set nombre=':inombre',
                direccion=':idireccion',
                telefono=:itelefono , 
                num_cama=:inum_cama
                where Plantilla_cod=:Plantilla_cod
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( Plantilla_cod , nombre , direccion , telefono , num_cama ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros



