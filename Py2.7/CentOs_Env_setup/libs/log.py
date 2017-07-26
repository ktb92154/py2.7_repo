import logging
from logging.config import fileConfig

#fileConfig('C:\Users\J15865\PycharmProjects\CentOs_Env_setup\config\logging.ini') # Works
fileConfig('..\..\config\logging.ini') # Works

logger = logging.getLogger()

HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[1;32m'
WARNING = '\033[93m'  # Yellowish
RED = '\033[1;31m'
# FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = "\033[1m"
UNDERLINE = '\033[4m'


def disable():
	HEADER = ''
	BLUE = ''
	GREEN = ''
	WARNING = ''
	FAIL = ''
	ENDC = ''
	UNDERLINE = ''


def print_format_table():
	for style in range(8):
		for fg in range(30, 38):
			s1 = ''
			for bg in range(40, 48):
				format = ';'.join([str(style), str(fg), str(bg)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
			print(s1)


def good(msg):
	print (GREEN + msg + ENDC)


def debug(msg):
	logger.debug(msg)
	# print (BLUE + msg + ENDC)


def info(msg):
	logger.info(msg)
	# print (BLUE + msg + ENDC)


def warn(msg):
	logger.warning(msg)
	# print (WARNING + msg + ENDC) # Not needed, logger prints to terminal


def err(msg):
	logger.error(msg)
	# print (RED + msg + ENDC) # Not needed, logger prints to terminal
