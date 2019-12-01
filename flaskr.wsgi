# 
import os
import sys
sys.path.insert(0, '/var/www/env/flaskr')


from main import app as application
application.root_path = '/var/www/env/flaskr'

