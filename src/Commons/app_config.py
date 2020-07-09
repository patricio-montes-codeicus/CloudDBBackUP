from Commons.singleton import singleton
from configparser import ConfigParser

config = ConfigParser()
config.read('./app_config.ini')

@singleton
class APPConfig:
    def __init__(self):
        """"""
    #Section: Data Base Drivers
    driver_sql = config.get('Drivers', 'SQL')
    driver_mysql = config.get('Drivers', 'MYSQL')
    driver_ase = config.get('Drivers', 'SYBASE')

    #Section: Google Drive Parameters
    google_drive_name = config.get('GoogleDrive', 'product_name') 
    google_drive_version = config.get('GoogleDrive', 'product_version')
    google_drive_endpoint = config.get('GoogleDrive', 'endpoint')

    #Section: App Files
    file_backup_path = config.get('Files', 'file_backup_path') 
    file_log_path = config.get('Files', 'file_log_path')


