from flask import Flask, render_template, request, redirect
from forms.loginForm import LoginForm
from forms.registerForm import RegisterForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SUPER_SECRET_KEY'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


app.run(debug=True)
