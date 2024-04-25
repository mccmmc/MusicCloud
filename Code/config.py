from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
