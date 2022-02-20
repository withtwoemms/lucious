from os import environ as envvars
from distutils.util import strtobool


PROJECT_NAME = 'lucious'

COVERAGE = bool(strtobool(envvars.get('COVERAGE', 'True')))
OFFICIAL = bool(strtobool(envvars.get('OFFICIAL', 'False')))
VENV = f'{PROJECT_NAME}-venv'
TESTDIR = f'tests.{PROJECT_NAME}'
TESTNAME = envvars.get('TESTNAME', '')
USEVENV = envvars.get('USEVENV', False)

