from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from Clients.google_drive import IGoogleDrive
from ClientsImpl.google_api_security_impl import GoogleApiSecurityImpl


class GoogleDriveImpl(IGoogleDrive):

    def upload_simple_file(self, file_path):
        
        api_security = GoogleApiSecurityImpl()
        DRIVE = build('drive', 'v3', http=api_security.google_drive_authenticate().authorize(Http()))

        FILES = (
            ('TestQuickStart.txt'),
        )

        for file_title in FILES :
            file_name = file_title
            metadata = {'name': file_name,
                        'mimeType': None
                        }

            res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
            if res:
                print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))


    def upload_resumable_file(self):
        return None