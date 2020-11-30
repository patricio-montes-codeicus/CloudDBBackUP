import pyodbc

print("Estableciendo conexion")
input()
conn = pyodbc.connect('DRIVER={Devart ODBC Driver for MySQL};User ID=root;Password=root;Server=localhost.mysql;Database=test;Port=3307;OPTION=3', autocommit=True)

cursor = conn.cursor()
cursor.execute('SELECT 1')

for row in cursor.fetchall():
    print(row)