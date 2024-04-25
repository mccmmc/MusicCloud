from flask import request, Blueprint, render_template, url_for
import os

main_page = Blueprint('index', __name__, static_folder='static', template_folder='templates')


def get_tracks(user):
    tracks = []
    directory = os.getcwd() + f'/static/music_library/{user}'
    print(os.listdir(directory))
    track_dirs = os.listdir(directory)
    for i in track_dirs:
        print(i)
        track_info = {}
        with open(directory + f'/{i}/track_info.txt', 'r', encoding="UTF8") as file:
            data = [i.strip() for i in file.readlines()]
            print(data)
            track_info["name"] = data[0]
            track_info["type"] = data[1]
            track_info["duration"] = data[2]
            track_info["img"] = data[3]
            track_info["path"] = f'{user}/{i}/track.mp3'
        tracks.append(track_info)
    print(tracks)
    return tracks


@main_page.route('/')
def results():
    tracks = get_tracks("mccmmc")
    return render_template("index.html", tracks=tracks)
