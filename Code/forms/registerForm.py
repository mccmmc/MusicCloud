from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()], render_kw={"placeholder": "Логин"})
    password = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Пароль"})
    password_again = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Повторите пароль"})
    token = PasswordField(validators=[DataRequired()], render_kw={"placeholder": "Введите токен"})
    submit = SubmitField('Зарегистрироваться')