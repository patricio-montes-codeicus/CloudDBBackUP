from src.Clients.google_api_security import IGoogleApiSecurity
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

class GoogleApiSecurityImpl(IGoogleApiSecurity):

    def google_drive_authenticate(self):

            try :
                import argparse
                flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
            except ImportError:
                flags = None

            SCOPES = 'https://www.googleapis.com/auth/drive.file'
            store = file.Storage('./storage.json')
            creds = store.get()
            if not creds or creds.invalid:
                print("make new storage data file ")
                flow = client.flow_from_clientsecrets('./google_api_credentials.json', SCOPES)
                creds = tools.run_flow(flow, store, flags) \
                    if flags else tools.run(flow, store)
            else:
                return creds