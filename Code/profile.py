from flask import request, Blueprint, render_template, url_for, redirect
from flask_login import current_user
import flask_login
import os

profile_page = Blueprint('profile', __name__, static_folder='static', template_folder='templates')


@profile_page.route('/')
def results():
    if not(current_user.is_authenticated):
        return redirect('/login')
    return render_template("profile.html")
