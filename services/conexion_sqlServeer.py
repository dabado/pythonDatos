import pyodbc

#conection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost;DATABASE=HOSPITAL;UID=SA;password=Getafe12345@@ ;TrustServerCertificate=yes')
conection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
if conection:
    print(f".....conexion correcta {conection}")
else:
    print("fallo de conexion")
print("funciona")
sql="select APELLIDO from EMP"
cursor= conection.cursor()
cursor.execute(sql)
datos = []
for row in cursor:
    datos.append(row)
print(f"resultados:   {datos}")
cursor.close()
conection.close()