import os

class config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\x9e\x0f\xe0\x13\x89\xd3\x8bP\xef:5\xdd\x8e\nI\x1f'"
    
    MONGODB_SETTINGS = {'db' : 'UTA_Enrollment'}