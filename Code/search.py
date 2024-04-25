from flask import request, Blueprint, render_template, redirect, session
from seach_sistem.search import search_tracks, create_client
from seach_sistem.Download import download_track

search_sistem = Blueprint('search_sistem', __name__, static_folder='static', template_folder='templates')


@search_sistem.route('/')
def mars():
    return render_template('search.html', title='Поиск')


@search_sistem.route('/result', methods=['POST'])
def search():
    query = request.form['Search_music']
    print(type(query))
    print(query)
    resp = search_tracks(create_client('AQAAAAAUjRFAAAG8Xn57pRR2lU7mqYicZyxhLlQ'), query)

    session.modified = True

    session['req'] = query

    print(resp)
    return render_template('search_results.html', tracks=resp)


@search_sistem.route('/download/<trck>')
def download(trck):
    print(trck)

    music = session[trck]
    print('music -', music)

    download_track(music, 'mccmmc')
    return redirect('/main', )
