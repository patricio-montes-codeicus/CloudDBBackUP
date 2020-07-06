import pyodbc 
from DBConnections.expected_connection import ExpectedConnection
from DBConnections.connection_factory import DBConnectionFactory

expected_connection = ExpectedConnection()


print("Tipo de Host 1-SQL 2-Oracle 3-Sybase 4-Postgress 5-MySQL")
expected_connection.typehost = input()
print("Host:")
expected_connection.host = input()
print("Port:")
expected_connection.port = input()
print("Username:")
expected_connection.username = input()
print("password:")
expected_connection.password = input()
print("DataBase:")
expected_connection.database = input()

factory_connection = DBConnectionFactory(expected_connection)
db_connection = factory_connection.create_connection("SQL")

conn = pyodbc.connect(db_connection.build_connection(expected_connection.get_db_type(int(expected_connection.typehost))))
cursor = conn.cursor()

#Sample select query
cursor.execute(db_connection.build_query_backup(expected_connection.database)) 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()