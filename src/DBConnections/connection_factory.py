from abc import ABCMeta, abstractstaticmethod
from Commons.singleton import singleton
from ServicesImpl.file_manager_impl import FileManagerImpl
import datetime
from Commons.app_config import APPConfig

app_config = APPConfig()

class IDBConnection(metaclass=ABCMeta):  

    @abstractstaticmethod
    def build_connection(self, expected_connection):
        """Build data-source connection"""

    @abstractstaticmethod
    def build_query_backup(self, query):
        """ Build query backup to execute """

@singleton
class SQLServerConnection(IDBConnection):  

    def build_connection(self, con):
            if con.port != '':
                con.port = ',' + con.port
            return 'DRIVER=' + app_config.driver_sql + ';SERVER=' + con.host + con.port + ';DATABASE=' + con.database + ';UID='+ con.username + ';PWD=' + con._password
               
               
    def build_query_backup(self, db_name, absolute_backup_path):
            return 'BACKUP DATABASE ' + '[' + db_name + ']' + ' TO DISK = ' + '\'' + absolute_backup_path + '\'' +  ';'


class DBConnectionFactory: 

    def create(self, type_host):
        try:
            if type_host == 'SQL':
                return SQLServerConnection()
            if type_host == 'ASE':
                return SQLServerConnection()
            if type_host == 'MYSQL':
                return SQLServerConnection()
            raise AssertionError("Connection Not Found")
        except AssertionError as _e:
            print(_e)
        return None