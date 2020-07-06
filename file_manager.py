import os.path

class FileManager:

    def read_all_bytes(self, path_file):
         if os.path.exists(path_file):
             # This is the default mode. It Opens file for reading.
             file = open(path_file, "r")
             return file.read()
