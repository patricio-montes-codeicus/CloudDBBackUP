from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools
from Clients.google_drive import IGoogleDrive
from ClientsImpl.google_api_security_impl import GoogleApiSecurityImpl
import os
from Commons.app_config import APPConfig

app_config = APPConfig()

class GoogleDriveImpl(IGoogleDrive):

    def upload_simple_file(self, file_path):

        api_security = GoogleApiSecurityImpl()
        DRIVE = build(app_config.google_drive_name, app_config.google_drive_version, http=api_security.google_drive_authenticate().authorize(Http()))

        FILES = (
            (file_path),
        )

        for file_title in FILES :
            file_name = file_title
            metadata = {'name': file_name,
                        'mimeType': None
                        }

            res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
            if res:
                print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))


    def upload_resumable_file(self, file_path):
        
        api_security = GoogleApiSecurityImpl()
        DRIVE = build(app_config.google_drive_name, app_config.google_drive_version, http=api_security.google_drive_authenticate().authorize(Http()), cache_discovery=False)
        file_name = os.path.basename(file_path)
        media_body = MediaFileUpload(file_path, mimetype='application/octet-stream', resumable=True)
        metadata = {'name': file_name,
                    'mimeType': None
                   }
        print("Uploading file...")
        res = DRIVE.files().create(body=metadata, media_body=media_body).execute()
        if res:
            print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))