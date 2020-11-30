import paramiko
import os

def main():
    
    # Connection with powershell
    # os.system('powershell.exe ssh wslroot@10.16.172.3')

    # Connection and exec command with paramiko.
    try: 
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("Estableciendo conexión...")
        client.connect(hostname='10.16.172.3', username='wslroot', password='ubuntur00t')
        print("conectado")
        session = client.get_transport().open_session()
        print('sesión establecida')
        if session.active:
            print('sesión activa')
            session.exec_command('ls')

            result = session.recv(1024).decode()
            print(result)

        client.close()

    except paramiko.ssh_exception.AuthenticationException as e:
        print('Error de autenticación: ' + str(e))

if __name__ == "__main__":
    # execute only if run as a script
    main()