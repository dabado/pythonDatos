import oracledb
from models import sala 
  # inscripcion , apellido , direccion, fecha_nac, sexo, nss


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

    def insertarEnfermo(self,inscripcion , apellido , direccion, fecha_nac, sexo, nss):
        sql="insert into Enfermo values(:inscripcion , :apellido , :direccion , :fecha_nac , :sexo , :nss)"
        cursor=self.conexion.cursor()
        cursor.execute(sql, (inscripcion , apellido , direccion, fecha_nac, sexo, nss))
        registrosAfectados=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"insertamos: {registrosAfectados}")
        return registrosAfectados

    def eliminarEnfermo(self, idEnfermo):
        sql="delete from Enfermo where inscripcion=:inscripcion"
        cursor = self.conexion.cursor()        
        cursor.execute(sql, (idEnfermo, ))
        registros = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros

    def modificaEnfermo(self, inscripcion , apellido , direccion, fecha_nac, sexo, nss):
        sql="""
                update Enfermo 
                set inscripcion=':inscripcion',
                apellido=':apellido'
                direccion=':direccion',
                fecha_nac=':fecha_nac' , 
                sexo=':sexo',
                nss=:nss
                where inscripcion=:inscripcion
            """
        cursor = self.conexion.cursor()        
        cursor.execute(sql, ( inscripcion , apellido , direccion, fecha_nac, sexo, nss ))
        registros=cursor.rowcount
        self.conexion.commit()
        cursor.close()
        print(f"modificados: {registros} registros")
        return registros



