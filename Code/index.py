import flask_login
from flask_login import login_required
from flask import request, Blueprint, render_template, url_for
import os

main_page = Blueprint('index', __name__, static_folder='static', template_folder='templates')

def get_tracks(user):
    tracks = []
    directory = os.getcwd() + f'/static/music_library/{user}'
    try:
        track_counts = len(os.listdir(directory))
    except FileNotFoundError:
        return []
    for i in range(track_counts):
        track_info = {}
        with open(directory + f'/{i + 1}/track_info.txt', 'r', encoding="UTF8") as file:
            data = [i.strip() for i in file.readlines()]
            track_info["name"] = data[0]
            track_info["type"] = data[1]
            track_info["duration"] = data[2]
        track_info["img_path"] = f"music_library/{user}/{i + 1}/track.jpg"
        tracks.append(track_info)
    return tracks


@main_page.route('/')
@login_required
def mars():
    tracks = get_tracks(str(flask_login.current_user.id))
    return render_template("index.html", tracks=tracks)
