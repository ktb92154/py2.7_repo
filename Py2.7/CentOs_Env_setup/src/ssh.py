from paramiko import client
import ftplib
import time
import os
import sys
import traceback

# https://daanlenaerts.com/blog/2016/07/01/python-and-ssh-paramiko-shell/

class ssh:
	client = None

	def __init__(self, address, username, password):
		self.server = address
		self.username = username
		self.password = password

		self.client = client.SSHClient()
		self.client.set_missing_host_key_policy(client.AutoAddPolicy())
		self.client.connect(self.server, username=username, password=password, look_for_keys=False)
		if self.client:
			print("Connected to server: " + str(self.server))
		else:
			print("Failed to connect to server: " + str(self.server))

	def __del__(self):
		if self.client:
			self.client.close()
			print("Disconnected from server: " + self.server)

	def sendCommand(self, command):
		if self.client:
			stdin, stdout, stderr = self.client.exec_command(command)
			while not stdout.channel.exit_status_ready():
				# Print data when available
				if stdout.channel.recv_ready():
					alldata = stdout.channel.recv(1024)
					prevdata = b"1"
					while prevdata:
						prevdata = stdout.channel.recv(1024)
						alldata += prevdata

					print ('-------------------------------------------------------------\n' +\
						'Command: ' + command + '\n' +\
						'Result: ' +'\n'+\
						  alldata +\
						  '-------------------------------------------------------------\n')
					return alldata
		else:
			print("Connection not opened.")

	def sendCommands(self, cmdFile):
		if self.client:

			with open(cmdFile, 'r') as file:
				my_list = file.readlines()
				file.close()

			print my_list

			i = 0
			for f in my_list:
				i += 1
				self.sendCommand(f)
				print 'Sent cmd ' + str(i) + ' of ' + str(len(my_list))
				time.sleep(0.05)

		else:
			print("Connection not opened.")