import pyodbc

conection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=HOSPITAL;UID=SA;password=Getafe12345@@ ;TrustServerCertificate=yes')
print("funciona")
sql="select APELLIDO from EMP"
cursor= conection.cursor()
cursor.execute(sql)
datos = []
for row in cursor:
            
    datos.append(row)
print(datos)