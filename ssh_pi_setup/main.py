import paramiko
from paramiko import client

server = "192.168.4.151"
user = "pi"
password = "raspberry"

class ssh:
    client = None

    def __init__(self, address, user, password):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, username=user, password=password, look_for_keys=False)

    def sendCommand(self, command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata

                    print(str(alldata, "utf8"))
        else:
            print("Connection not opened.")


connection = ssh(server, user, password)
connection.sendCommand("ls")
connection.sendCommand("cd Desktop")
connection.sendCommand("mkdir testfolder")
connection.sendCommand("cd testfolder && mkdir testfolder2")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #RSA key fingerprint is
ssh.connect(server, username=user, password=password)
stdin, stdout, stderr = ssh.exec_command('sudo apt-get upgrade -y')
#stdin.write('test\n')
stdout.flush()
stderr.flush()
print stdout.read()
print stderr.read()