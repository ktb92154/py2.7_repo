"""
testing autodoc - this should be first line in doc
"""
from ssh import ssh


class main():
	"""
	testing autodoc - this should be first line in doc
	"""
	# server = "10.175.9.211"
	server = "10.175.9.209"
	user = "root"
	password = "hun_system"

	connection = ssh(server, user, password)
	connection.sendCommand("ls")
	connection.sendCommand("cd Desktop")
	connection.sendCommand("mkdir testfolder")
	connection.sendCommand("ls")

	print'change ISO to vmware-tools'

	test = connection.sendCommand('/etc/init.d/vmware-tools status')
	print test
	if 'running' not in test:
		print'change ISO to vmware-tools'
		result = connection.sendCommand('sudo mount /dev/cdrom /mnt/cdrom')
		print result


# connection.sendCommands('test.txt')

if __name__ == "__main__":
	main()
