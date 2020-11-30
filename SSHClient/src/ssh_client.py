import paramiko

class SSHClient:

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def get_connection(self, hostname, port, username, password):
        try:
            print("Estableciendo conexión...")
            client.connect(hostname=hostname, port=port, username=username, password=password)
            print("Conectado")
            return client.get_transport().open_session()

        except paramiko.ssh_exception.AuthenticationException as e:
            print('Error de autenticación: ' + str(e))

    def send_command(self, command, connection):
        if connection.active:
            print('Sesión activa')
            session.exec_command(command)

            result = session.recv(1024).decode()
            connection.close()
            return result
        else:
            print('Sesión caducada')