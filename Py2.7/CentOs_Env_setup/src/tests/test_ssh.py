from ..ssh import ssh
import pytest

@pytest.fixture()
def fixture01(request):
    print("\nIn fixture...")
    print("Fixture Scope: " + str(request.scope))
    print("Function Name: " + str(request.function.__name__))
    print("Class Name: " + str(request.cls))
    print("Module Name: " + str(request.module.__name__))
    print("File Path: " + str(request.fspath))


server = "10.175.9.209"
user = "root"
password = "hun_system"

@pytest.mark.usefixtures('fixture01')
def test_connection():
	connection = ssh(server, user, password)

@pytest.mark.usefixtures('fixture01')
def test_sendCommand():
	connection = ssh(server, user, password)
	print connection.sendCommand("ls")

@pytest.mark.usefixtures('fixture01')
def test_sendCommands():
	connection = ssh(server, user, password)
	print connection.sendCommands("test_cmds")

'''print "Logging in..."
ftp = ftplib.FTP()
ftp.connect(server)
print ftp.getwelcome()
try:
	try:
		ftp.login(user, password)
		ftp.cwd('target directory')
		# move to the desired upload directory
		print "Currently in:", ftp.pwd()

		print "Uploading...",
		fullname = '../sourcedirectoy/filename'
		name = os.path.split(fullname)[1]
		f = open(fullname, "rb")
		ftp.storbinary('STOR ' + name, f)
		f.close()
		print "OK"

		print "Files:"
		print ftp.retrlines('LIST')
	finally:
		print "Quitting..."
		ftp.quit()
except:
	traceback.print_exc()'''