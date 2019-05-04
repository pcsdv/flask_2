
from flask import Blueprint,render_template,redirect, url_for,request,flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import  UserMixin,login_required, logout_user, current_user,login_user
from flask import current_app 
from sqlalchemy import create_engine
#from myapp import loginmanager # extension instance

from myapp import  db, mysql, bmysql
 

users = Blueprint('users',__name__,template_folder='templates')


@users.route('/user')
def index():
    return render_template('users/users.html')


# extras --------------------

@users.route('/extras',methods=['GET','POST'])
def extras():
	cur = bmysql.connect()
	cr = cur.cursor()
	cr.execute("SELECT * FROM dems_patient")
	rows = cr.fetchall()
	data = [row for row in rows]
	cur.close()
	return render_template('users/extras.html',title='Extras', fts=data )


@users.route('/extras/<username>',methods=['GET','POST'])
def show_extras(username):
	cur = bmysql.connect()
	cr = cur.cursor()
	cr.execute("SELECT * FROM dems_patient WHERE name LIKE %s",[username])
	cv = cr.fetchall()
	cur.close()
	return render_template('users/extras1.html',title='Extras1',sr = cv)


@users.route('/search_extras',methods = ['GET','POST'])
def search_extras():
	if request.method == 'POST':
		conn = bmysql.connect()
		cr= conn.cursor()
		cr.execute("SELECT * FROM dems_patient WHERE name LIKE %s",request.form['servs'])
		conn.close()
		return render_template("users/extras.html",title='extras_search',ns =cr.fetchall())

	return render_template('users/extras.html',title='Extras')

# bio -------------------------

@users.route('/bio',methods=['GET','POST'])
def bio():
	cur = mysql.connect()
	cr = cur.cursor()
	cr.execute("SELECT * FROM dems_biochemic")
	rows = cr.fetchall()
	data = [row for row in rows]
	cur.close()
	return render_template('users/bio.html',title='Bio', fts=data )

@users.route('/bio/<username>',methods=['GET','POST'])
def show_bio(username):
	cur = mysql.connect()
	cr = cur.cursor()
	cr.execute("SELECT * FROM dems_biochemic WHERE name LIKE %s",[username])
	cv = cr.fetchall()
	cur.close()
	return render_template('users/bio1.html',title='bio1',sr = cv)


@users.route('/search_bio',methods = ['GET','POST'])
def search_bio():
	if request.method == 'POST':
		conn = mysql.connect()
		cr= conn.cursor()
		cr.execute("SELECT * FROM dems_biochemic WHERE name LIKE %s",request.form['servs'])
		conn.close()
		return render_template("users/bio.html",title='bio_search',ns =cr.fetchall())

	return render_template('users/bio.html',title='Bio')
# -------------------------
#@app.route("/medicine", methods=['GET', 'POST'])
#def medicine():
#	con = engine.connect()
#	result = con.execute('SELECT * FROM dems_patient')

#	con.close()
#	return render_template('medicine.html',title='Medicine',tdata=result)

# ------------------------------
@users.route("/medicine", methods=['GET', 'POST'])
def medicine():
	engine = create_engine('mysql://prokash:q1234q123@localhost/flask')
	con = engine.connect()
	result = con.execute('SELECT * FROM daily_extras')

	con.close()
	return render_template('users/medicine.html',title='Medicine',tdata=result)


@users.route("/medicine/<username>", methods=['GET', 'POST'])
def show_medicine(username):
	engine = create_engine('mysql://prokash:q1234q123@localhost/flask')
	con = engine.connect()
	show = con.execute('SELECT * FROM daily_extras WHERE date LIKE %s',[username])
	con.close()
	return render_template('users/medicine1.html',title='Medicine1',td=show)

@users.route("/searchmedicine", methods=['GET', 'POST'])
def search_medicine():
	if request.method == "POST":
		engine = create_engine('mysql://prokash:q1234q123@localhost/flask')
		con = engine.connect()
		result = con.execute('SELECT * FROM daily_extras WHERE date LIKE %s',request.form['medsearch'])
		con.close()
		return render_template('users/medicine.html',title='Medicine_search',stdata=result)
	else:	
		return render_template('users/medicine.html',title='Medicine')
#----------------------------

@users.route('/crdb',methods=['GET','POST'])
def crdb():
	cur = mysql.connect()
	cr = cur.cursor()
	cr.execute("SELECT * FROM home_crdb")
	rows = cr.fetchall()
	data = [row for row in rows]
	cur.close()
	return render_template('users/crdb.html',title='Crdb', fts=data )

@users.route('/crdb/<username>',methods=['GET','POST'])
def show_crdb(username):
	cur = mysql.connect()
	cr = cur.cursor()
	cr.execute("SELECT * FROM home_crdb WHERE name LIKE %s",[username])
	cv = cr.fetchall()
	cur.close()
	return render_template('users/crdb1.html',title='Crdb1',sr = cv)


@users.route('/search_crdb',methods = ['GET','POST'])
def search_crdb():
	if request.method == 'POST':
		conn = mysql.connect()
		cr= conn.cursor()
		cr.execute("SELECT * FROM home_crdb WHERE name LIKE %s",request.form['crdbs'])
		conn.close()
		return render_template("users/crdb.html",title='Crdb_search',ns =cr.fetchall())

	return render_template('users/crdb.html',title='Crdb')
# -------------------------
