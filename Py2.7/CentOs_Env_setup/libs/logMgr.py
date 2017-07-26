#/==============================================================================
#/
#/ Unclassified                  U N C L A S S I F I E D           Unclassified
#/
#/ FILE:                         logMgr.py
#/
#/ DESCRIPTION:         Python script to configure AMMS switches and boards
#/                      
#/
#/ AUTHOR:          K. Burgess
#/
#/ COMPANY:         Northrop Grumman Corporation
#/ SECTOR:          Aerospace Systems
#/ BUSINESS AREA:   HALE Enterprise Mission Systems
#/ ADDRESS:         17066 Goldentop Road
#/                  340-2C Building 2
#/                  San Diego, CA 92127-2412
#/
#/ PROJECT:         Unmanned Systems                   
#/ CONTRACT:        Northrop Grumman Aerospace Systems            
#/ CSCI:            AMMS
#/ CSC:             SCRIPTS
#/
#/ CHANGE HISTORY:
#/
#/ Date         Description of Change                                Programmer
#/ ---------    -------------------------------------------------    -----------
#/ 02/25/15    Initial Release                                       K. Burgess
#/ 03/26/15    Added Capability v1.0                                 K. Burgess
#/==============================================================================
############################################################################### 
#!/usr/bin/python
import dirMgr
import logging
import logging.config
import ConfigParser
import os
import datetime


loggers = {}

class logger(object):
	global cfg, loggers, dirMgr
	dirMgr = dirMgr.mgr()
	cfgFile = dirMgr.get_cfg()
	cfg = ConfigParser.ConfigParser()
	cfg.read(cfgFile)
	# Constructor
	def __init__(self, name = 'root', logFile=cfg.get('logs', 'main')):
		self.name = name
		self.date = ''
		self.dateFormat = ''
		self.home = ''
		self.logFileType = cfg.get('file','log')
		self.setLogDate()
		self.folderPath = dirMgr.set_logs_dir(self.dateFormat)
		self.logFile = str(self.folderPath) + str(logFile)
		if not (cfg.get('logs', 'main') in self.logFile):
			self.logFile = self.folderPath + ( '%s%02d%s%02d%s%02d%s' % ( 
			(logFile + '_', self.date.hour, ':', self.date.minute
			, ':', self.date.second, self.logFileType)))
 
			print 'Changed log file to: ' +self.logFile		

		self.myLogger()
	
	def get_logs_dir(self):
		return self.folderPath

	def get_logs_file(self):
		return self.logFile

	def setLogDate(self):
		'''
		Create date for log folder creation
		'''
		self.date = datetime.datetime.now()
                self.dateFormat = ('%s%02d%02d' % (self.date.year, self.date.month,
                                                self.date.day))

	def myLogger(self):
		if loggers.get(self.name):
			return loggers.get(self.name)
		else:
			logger = logging.getLogger(self.name)
			logging.config.fileConfig('logging.cfg',
						defaults={'logfilename': self.logFile} ,
						disable_existing_loggers=False)
			loggers.update(dict(name=logger))
			return logger

	def clean(self, txt):
                #print txt
                #str = txt
		str = repr(txt)
                str = str.strip()
                str = str.replace('\\r', '')
                str = str.replace('\\t', '    ')
                #str = str.replace('\\t', '\t')
                str = str.replace('\\r', '')
                str = str.replace('\\x1b', '')
                str = str.replace('[K', '')
                str = str.replace('[100B', '')
                str = str.replace('[27m', '')
		str = str.replace('\\n', '\n')
		str = str.replace('\\', '')
                str = str.replace('x08', '')
		return str

	def info(self, txt):
		str = self.clean(txt)
		logger = logging.getLogger(self.name)
		#logging.info( '\033[93m' + str + '\033[0m' )
		logger.info(str)		
	 
	def debug(self, txt):
		str = self.clean(txt)
		logger = logging.getLogger(self.name)
		logger.debug(str)

	def warning(self, txt):
		str = self.clean(txt)
		logger = logging.getLogger(self.name)
		#logger.warning('\033[93m' + str)
		logger.warning(str)		

	def error(self, txt):
		str = self.clean(txt)
		logger = logging.getLogger(self.name)
		#logger.error('\033[93m' + str + '\033[0m')		
		logger.error(str)		
#---------------------------------------------------------------------------
#*******************************UNCLASSIFIED********************************
#***************************************************************************
#***                                                                     ***
#***  U   U NN   N  CCCC L      AAA   SSSS  SSSS I FFFFF I EEEEE DDDD    ***
#***  U   U N N  N C     L     A   A S     S     I F     I E     D   D   ***
#***  U   U N  N N C     L     AAAAA  SSS   SSS  I FFFF  I EEEE  D   D   ***
#***  U   U N   NN C     L     A   A     S     S I F     I E     D   D   ***
#***   UUU  N    N  CCCC LLLLL A   A SSSS  SSSS  I F     I EEEEE DDDD    ***
#***                                                                     ***
#***************************************************************************
#*******************************UNCLASSIFIED********************************
#---------------------------------------------------------------------------
