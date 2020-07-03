import pyodbc 
from DBConnections.connection_spected import ConnectionSpected
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

PATH_FILE = '\'' + 'C:\DBBackUP' + '\\' + '\''

obj = ConnectionSpected()

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

server = obj.host + ',' + obj.port 
database = obj.database 
username = obj.username 
password = obj.password 

cnxn = pyodbc.connect('DRIVER='+obj.DRIVER+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

QUERY_BACKUP = 'BACKUP DATABASE ' + '[' + obj.database + ']' + ' TO DISK = ' + PATH_FILE + ';'
print(QUERY_BACKUP)

#Sample select query
cursor.execute(QUERY_BACKUP) 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()