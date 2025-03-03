import pymysql

conection = pymysql.connect( host='localhost', port=3306, user='getafe', password='mysql', database='HOSPITAL')
if conection:
    print(f".....conexion correcta {conection}")
else:
    print("fallo de conexion")
sql=""" select * 
        FROM EMP 
        where SALARIO >= %s"""
print("introduzca un salario")
salario=int(input())
cursor= conection.cursor()
cursor.execute(sql, (salario, ))
for row in cursor:
    print(f"resultados para mayor de {salario}:  {row[0]}, {row[1]},{row[2]},{row[3]},{row[4]}")
cursor.close()
conection.close()