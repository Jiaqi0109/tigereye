import os

class DefalutConfig(object):

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jiaqi0109@localhost/tigereye'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    LOG_DIR = os.path.join(BASE_DIR, 'logs')
