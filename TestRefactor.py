import pyodbc 
from DBConnections.connection_expected import ConnectionExpected
from DBConnections.connection_factory import DBConnectionFactory

obj = ConnectionExpected()


print("Tipo de Host 1-SQL 2-Oracle 3-Sybase 4-Postgress 5-MySQL")
obj.typehost = input()
print("Host:")
obj.host = input()
print("Port:")
obj.port = input()
print("Username:")
obj.username = input()
print("password:")
obj.password = input()
print("DataBase:")
obj.database = input()

objtwo = DBConnectionFactory(obj)
objs = objtwo.create_connection(obj)


cnxn = pyodbc.connect(objs.build_connection(obj))
cursor = cnxn.cursor()


#Sample select query
cursor.execute(objs.build_query_backup("obj.database")) 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()