import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Base configuration

    Args:
        object (_type_): _description_
    """

class DevConfig(Config):
    """Development config

    Args:
        Config (_type_): _description_
    """

class ProConfig(Config):
    """Production config

    Args:
        Config (_type_): _description_
    """

class TestingConfig(Config):
    """Testing config

    Args:
        Config (_type_): _description_
    """
    TESTING = True