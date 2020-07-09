import os.path
from abc import ABCMeta, abstractstaticmethod

class IGoogleApiSecurity(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def google_drive_authenticate(self):
        """ Autentication by credentials or storage file """
