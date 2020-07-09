from abc import ABCMeta, abstractstaticmethod


class IFileManager(metaclass=ABCMeta):

    @abstractstaticmethod
    def get_absolute_path_backup(self, db_name, db_type):
        """ Construye y retorna la ruta del backup y su extensión correspondiente. """

    @abstractstaticmethod
    def get_backup_size(self, backup_path):
        """ Obtiene el tamaño en KB del archivo backup generado. """