from flask import request, Blueprint

search = Blueprint('search', __name__)


@search.route('/')
def buff():
    return f"""<!DOCTYPE html>
<html>
<head>
  <title>Search Page</title>
</head>
<body>
  <h1>Search</h1>
  <form action="/search" method="POST">
    <input type="text" name="query" placeholder="Enter search">
    <button type="submit">Search</button>
  </form>
</body>
</html>"""


@search.route('/search', methods=['POST'])
def search():
    query = request.form['query']

    return f"""<!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>results</title>
      </head>
      <body>
          <p>{query}</p>
      </body>
    </html>"""
