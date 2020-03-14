import db_conf
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Database initialization
class Config(object):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://{user}:{pw}@localhost/flamant_rose'.format(user=db_conf.POSTGRES_USER,pw=db_conf.POSTGRES_PW)
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    JSON_SORT_KEYS = False
    JSON_ADD_STATUS = False
