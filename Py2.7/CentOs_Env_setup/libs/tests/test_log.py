from libs.log import *
import pytest


@pytest.fixture()
def fixture01(request):
	print("\nIn fixture...")
	print("Fixture Scope: " + str(request.scope))
	print("Function Name: " + str(request.function.__name__))
	print("Class Name: " + str(request.cls))
	print("Module Name: " + str(request.module.__name__))
	print("File Path: " + str(request.fspath))


@pytest.mark.usefixtures('fixture01')
def test_good():
	good('good test 01')

def test_debug():
	debug('debug test 01')

def test_debug():
	info('info test 01')

def test_debug():
	warn('warning test 01')

def test_err():
	err('error test 01')