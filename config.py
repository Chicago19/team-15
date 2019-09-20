from pathlib import Path

class Config(object):
    '''
    Listener Flask config fields
    '''
    TEMPLATE_FOLDER = Path('./templates')
    URL = 'http://127.0.0.1:5000/'
    DEBUG = True
    SECRET_KEY = 'ti248_.r82-n'
