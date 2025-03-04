import pyodbc


conection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=127.0.0.1;DATABASE=HOSPITAL;UID=SA;PWD=Getafe12345@@;TrustServerCertificate=yes')
if conection:
    print(f".....conexion correcta {conection}")
else:
    print("fallo de conexion")



sql=""" select * 
        FROM EMP 
        where SALARIO >= ? """
print("introduzca un salario")
salario=int(input())
cursor= conection.cursor()
cursor.execute(sql, (salario, ))
for row in cursor:
    print(f"resultados para mayor de {salario}:  {row[0]}, {row[1]},{row[2]},{row[3]},{row[4]}")
cursor.close()
conection.close()