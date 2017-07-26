all = ["test_module01"]


def setup_module(module):
    print("\nIn setup_module()...")

def teardown_module(module):
    print("\nIn teardown_module()...")

def setup_function(function):
    print("\nIn setup_function()...")

def teardown_function(function):
    print("\nIn teardown_function()...")

def test_case01():
    print("\nIn test_case01()...")

def test_case02():
    print("\nIn test_case02()...")