from abc import ABCMeta, abstractstaticmethod

class IGoogleDrive(metaclass=ABCMeta):

    @abstractstaticmethod
    def upload_simple_file(self, file_path):
        """ quickly transfer a small media file (5 MB or less) without supplying metadata """

    @abstractstaticmethod
    def upload_resumable_file(self):
        """ upload operation after a communication failure interrupts the flow of data (5 MB or greater) """