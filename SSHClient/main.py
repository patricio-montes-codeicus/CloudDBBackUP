from src.ssh_client import SSHClient
from src.client_params import ClientParams

def main():

client_params = ClientParams();

print("Host:")
client_params.host = input()
print("Username:")
client_params.username = input()
print("password:")
client_params.password = input()
print("command:")
client_params.command = input()

ssh_client = SSHClient();
ssh_client_connection = ssh_client.get_connection(hostname=client_params.host, username=client_params.username, password=client_params.password);
ssh_client.send_command(client_params.command, ssh_client_connection);

if __name__ == "__main__":
    # execute only if run as a script
    main()