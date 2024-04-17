from flask import request, Blueprint, render_template

main_page = Blueprint('index', __name__, static_folder='static', template_folder='templates')


@main_page.route('/')
def mars():
    return render_template("index.html")
