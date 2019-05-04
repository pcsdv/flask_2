
from flask import Flask
from myapp.config import Config
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt 
from myapp.models import User

from flaskext.mysql import MySQL 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

bcrypt = Bcrypt()
db = SQLAlchemy()
mysql = SQLAlchemy()
mysql = MySQL()
bmysql = MySQL()

def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	db.init_app(app)
	mysql.init_app(app)
	bmysql.init_app(app)
#	engine.init_app(app)
	login_manager.init_app(app)
	bcrypt.init_app(app)
	
	@login_manager.user_loader
	def load_user(user_id):
		return User.query.get(int(user_id))
	#db.create_all()

	# import all route modules bluprint
	from myapp.main.routes import main
	from myapp.auth.routes import auth
	from myapp.users.routes import users
	from myapp.posts.routes import posts

	# and register blueprints
	app.register_blueprint(main)
	app.register_blueprint(auth)
	app.register_blueprint(users)
	app.register_blueprint(posts)

	return app

