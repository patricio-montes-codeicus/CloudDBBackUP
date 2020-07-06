import os.path
from abc import ABCMeta, abstractstaticmethod

class IFileManager(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_last_backup_by_dbname(self, db_name):
        """Last DBBackUp by Name"""

    @abstractstaticmethod
    def file_upload_drive(self, path_file):
        """Send upload drive"""