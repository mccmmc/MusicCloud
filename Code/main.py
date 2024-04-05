from config import app
from auth import auth
from search import search

app.register_blueprint(auth, url_prefix='')
app.register_blueprint(search, url_prefix='src')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
