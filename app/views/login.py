from flask import render_template, flash, redirect, Flask, session, url_for, request, g
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from ..models import User
from ..forms import LoginForm
from app import app, lm, db


@lm.user_loader
def load_user(userid):
    if userid == u'None':
        return None
    else:
        return User.query.get(int(userid))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template("index.html",
                           title='NMS',
                           user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['username'] = form.username.data
            login_user(user, remember=session['remember_me'])
            return redirect(url_for('index'))
        else:
            return render_template('login.html', form=form, failed_auth=True)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
