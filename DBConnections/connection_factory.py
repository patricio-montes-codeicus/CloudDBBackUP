from abc import ABCMeta, abstractstaticmethod
from configparser import ConfigParser
import datetime


config = ConfigParser()
config.read('./DBConnections/connection_config.ini')
print(config.sections())

class IDBConnection(metaclass=ABCMeta):  

    @abstractstaticmethod
    def build_connection(self, expected_connection):
        """Build data-source connection"""

    @abstractstaticmethod
    def build_query_backup(self, query):
        """ Build query backup to execute """


class SQLServerConnection(IDBConnection):  

    def build_connection(self, con):
            if con.port != '':
                con.port = ',' + con.port
            return 'DRIVER=' + config.get('drivers', 'SQL') + ';SERVER=' + con.host + con.port + ';DATABASE=' + con.database + ';UID='+ con.username + ';PWD=' + con._password
               
               
    def build_query_backup(self, dbname):
        path_file_backup = '\'' + config.get('files', 'backup_file_path') + dbname + '_' + str(datetime.datetime.now()).replace(":", ".") + '.bak' + '\''
        return 'BACKUP DATABASE ' + '[' + dbname + ']' + ' TO DISK = ' + path_file_backup + ';'


class DBConnectionFactory: 

    def create(self, type_host):
        try:
            print(type_host)
            if type_host == "SQL":
                return SQLServerConnection()
            if type_host == "ASE":
                return SQLServerConnection()
            if type_host == "MYSQL":
                return SQLServerConnection()
            raise AssertionError("Connection Not Found")
        except AssertionError as _e:
            print(_e)
        return None