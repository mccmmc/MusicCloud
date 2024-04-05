from flask_login import LoginManager, login_user, login_required, logout_user
from forms.loginForm import LoginForm
from forms.registerForm import RegisterForm
from flask import render_template, redirect, Blueprint
from data import db_session
from data.users import User
from config import app

auth = Blueprint('auth', __name__)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_session.global_init("db/users.db")
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_session.global_init("db/users.db")
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.submit.data:
        print(1)
        user = User()
        user.username = form.username.data
        user.set_password(form.password.data)
        db_session.global_init("db/users.db")
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")
