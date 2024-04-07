from flask import request, Blueprint, render_template
from seach_sistem.search import search_tracks, create_client

search_sistem = Blueprint('search_sistem', __name__, static_folder='static', template_folder='templates')


@search_sistem.route('/')
def mars():
    return render_template('search.html', title='Поиск')


@search_sistem.route('/result', methods=['POST'])
def search():
    query = request.form['query']
    print(type(query))
    resp = search_tracks(create_client('AQAAAAAUjRFAAAG8Xn57pRR2lU7mqYicZyxhLlQ'), query)

    print(resp)

    return render_template('search_results.html', tracks=resp)
