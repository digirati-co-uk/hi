import os
import distutils.util

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = bool(distutils.util.strtobool(os.environ.get('DEBUG', 'True')))


class TestConfig(Config):
    TESTING = True
    DEBUG = True
