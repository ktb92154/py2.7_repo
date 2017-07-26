from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import src

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.txt', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='CentOs_Env_setup',
    version=src.__version__,
    #url='http://github.com/jeffknupp/CentOs_Env_setup/',
    license='Apache Software License',
    author='Keith Burgess',
    tests_require=['pytest'],
    install_requires=[#'Flask>=0.10.1',
                    'Paramiko>=2.2.1',
                    #'SQLAlchemy==0.8.2',
                    ],
    cmdclass={'test': PyTest},
    author_email='ktb92154@gmail.com',
    description='Automated REST APIs for existing database-driven systems',
    long_description=long_description,
    packages=['CentOs_Env_setup'],
    include_package_data=True,
    platforms='any',
    test_suite='CentOs_Env_setup.test.test_CentOs_Env_setup',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)