import paramiko

server = "192.168.4.151"
username = "pi"
password = "raspberry"

cmd_to_execute = 'whoami'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #RSA key fingerprint is
ssh.connect(server, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('sudo apt-get upgrade -y')
#stdin.write('test\n')
stdout.flush()
stderr.flush()
print stdout.read()
print stderr.read()