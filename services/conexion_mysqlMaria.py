import pymysql 

conection = pymysql.connect( host='localhost', port=3306, user='getafe', password='mysql', database='HOSPITAL')
if conection:
    print(f".....conexion correcta {conection}")
else:
    print("fallo de conexion")
sql="select APELLIDO FROM EMP"

cursor= conection.cursor()
cursor.execute(sql)
datos = []
for row in cursor:    
    datos.append(row)
print(f"resultados:   {datos}")
cursor.close()
conection.close()