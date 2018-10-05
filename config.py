import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = bool(os.environ.get('DEBUG', 'True'))


class TestConfig(Config):
    TESTING = True
    DEBUG = True
