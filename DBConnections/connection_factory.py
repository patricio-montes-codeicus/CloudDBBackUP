from abc import ABCMeta, abstractstaticmethod
from configparser import ConfigParser


config = ConfigParser()
config.read('./DBConnections/connection_config.ini')
print(config.sections())

class IDBConnection(metaclass=ABCMeta):  

    @abstractstaticmethod
    def build_connection(self, expected_connection):
        """Build data-source connection"""

    @abstractstaticmethod
    def build_query_backup(self, query):
        """ Build query to execute """


class SQLServerConnection(IDBConnection):  

    def __init__(self, expected_connection):
        self._host = expected_connection.host
        self._port = expected_connection.port
        self._database = expected_connection.database
        self._username = expected_connection._username
        self._password = expected_connection._password

    def build_connection(self, expected_connection):
            if self._port != '':
                self._port = ',' + self._port
            print('DRIVER=' + config.get('drivers', 'SQL') + ';SERVER=' + self._host + self._port + ';DATABASE=' + self._database + ';UID='+ self._username + ';PWD=' + self._password)       
            return 'DRIVER=' + config.get('drivers', 'SQL') + ';SERVER=' + self._host + self._port + ';DATABASE=' + self._database + ';UID='+ self._username + ';PWD=' + self._password
               
               
    def build_query_backup(self, dbname):
        return 'BACKUP DATABASE ' + '[' + dbname + ']' + ' TO DISK = ' + config.get('files', 'path_file') + ';'


""" class PostgreSQLConnection(IDBConnection):  

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def create_connection(self, expected_connection):
        return {"width": self._width, "depth": self._depth, "height": self._height}

class SybaseConnection(IDBConnection):  

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height} """


class DBConnectionFactory: 

    def __init__(self, expected_connection):
        self._expected_connection = expected_connection

    def create_connection(self, type_host):
        try:
            if type_host == "SQL":
                return SQLServerConnection(self._expected_connection)
            if type_host == "ASE":
                return SQLServerConnection(self._expected_connection)
            if type_host == "MYSQL":
                return SQLServerConnection(self._expected_connection)
            raise AssertionError("Chair Not Found")
        except AssertionError as _e:
            print(_e)
        return None


"""if __name__ == "__main__":
    CHAIR_FACTORY = ChairFactory().get_connection("SmallChair")
    print(CHAIR_FACTORY.dimensions())
"""