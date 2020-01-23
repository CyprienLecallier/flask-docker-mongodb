#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
from flask import render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, logout_user, login_required, current_user, UserMixin, login_user
from config import app, db


#############################
#  Gestion login
#############################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
	def __init__(self, username):
		self.username = username
		#self.status = db.users.find_one({"login" : username})["status"]

#	@staticmethod
#	def is_authenticated():
#		return True

#	@staticmethod
#	def is_active():
#		return True

#	@staticmethod
#	def is_anonymous():
#		return False

	def get_id(self):
		return self.username


@login_manager.user_loader
def load_user(username):
	u = db.users.find_one({"login": username})
	if not u:
		return None
	return User(username=u["login"])


@app.before_request
def make_session_permanent():
	session.permanent = True
	app.permanent_session_lifetime = datetime.timedelta(minutes=1)

###################################
#  Gestion des URLs
###################################

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		if current_user.is_authenticated:
			return redirect(url_for("accueil"))
		return render_template('login.html')
	else:
		login = request.form['login'].strip()
		password = request.form['password']
		user = db.users.find_one({'login': login})
		if user['password'] == password:
			u = User(username=login)
			login_user(u)
			session["username"] = login
			return redirect(url_for("accueil"))
		else:
			flash('Wrong password')
			return redirect(url_for('login'))


@app.route('/accueil', methods=['GET', 'POST'])
@login_required
def accueil():
	return render_template('accueil.html')


@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("login"))


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)

