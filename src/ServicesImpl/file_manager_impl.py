from Services.file_manager import IFileManager
from Commons.app_config import APPConfig
import os
import datetime

app_config = APPConfig()

class FileManagerImpl(IFileManager):

        def get_absolute_path_backup(self, db_name, db_type):
                extension = ""
                if db_type == 'SQL':
                        extension = '.bak'
                if db_type == 'ASE':
                        extension = '.bak'
                if db_type == 'MYSQL':
                        extension = '.bak'
                if extension == "":
                        raise AssertionError("DB Type Not Found")
                now = datetime.datetime.now()
                return app_config.file_backup_path + db_name + '_' + str(datetime.date.today()) + '_' + str(now.hour) + '.' + str(now.minute) + '.' + str(now.second) + extension

        def get_backup_size(self, backup_path):
                try:
                    if os.path.exists(backup_path):
                        return os.path.getsize(backup_path)
                except FileNotFoundError as _e:
                        print(_e)
                except IOError as _e:
                        print(_e)
                return None
