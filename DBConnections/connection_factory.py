from abc import ABCMeta, abstractstaticmethod
import connection_config as config

class IDBConnection(metaclass=ABCMeta):  

    @abstractstaticmethod
    def build_connection(self, connection_expected):
        """Build data-source connection"""

    @abstractstaticmethod
    def build_query_backup(self, query):
        """ Build query to execute """


class SQLServerConnection(IDBConnection):  

    def __init__(self, connection_expected):
        self._host = connection_expected.host
        self._port = connection_expected.port
        self._database = connection_expected.database
        self._username = connection_expected._username
        self._password = connection_expected._password

    def build_connection(self, connection_expected):
        return {'DRIVER=' + config.driver["SQL"] +
                ';SERVER=' + self._host + ',' + self._port + 
                ';DATABASE=' + self._database + 
                ';UID='+ self._username + 
                ';PWD=' + self._password}

    def build_query_backup(self, dbname):
        return {'BACKUP DATABASE ' + '[' + dbname + ']' + ' TO DISK = ' + config.path_file + ';'}


""" class PostgreSQLConnection(IDBConnection):  

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def create_connection(self, connection_expected):
        return {"width": self._width, "depth": self._depth, "height": self._height}

class SybaseConnection(IDBConnection):  

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def dimensions(self):
        return {"width": self._width, "depth": self._depth, "height": self._height} """


class DBConnectionFactory: 

    def __init__(self, connection_expected):
        self._connection_expected = connection_expected

    def create_connection(self, connection_expected):
        try:
            if self._connection_expected._type_host == "SQL":
                return SQLServerConnection(self._connection_expected)
            if self._connection_expected.type_host == "ASE":
                return SQLServerConnection(self._connection_expected)
            if self._connection_expected.type_host == "MYSQL":
                return SQLServerConnection(self._connection_expected)
            raise AssertionError("Chair Not Found")
        except AssertionError as _e:
            print(_e)
        return None


"""if __name__ == "__main__":
    CHAIR_FACTORY = ChairFactory().get_connection("SmallChair")
    print(CHAIR_FACTORY.dimensions())
"""