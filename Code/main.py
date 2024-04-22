from config import app
from auth import auth
from search import search_sistem
from index import main_page
from player import player

app.register_blueprint(auth, url_prefix='')
app.register_blueprint(search_sistem, url_prefix='/src')
app.register_blueprint(main_page, url_prefix="/main")
app.register_blueprint(player, url_prefix="/ply")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
