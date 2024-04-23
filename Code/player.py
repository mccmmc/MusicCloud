import os

from flask import request, Blueprint, render_template
from seach_sistem.search import search_tracks, create_client

player = Blueprint('player', __name__, static_folder='static', template_folder='templates')


@player.route('/')
def ply():
    user = 'mccmmc'
    default = f'./static/music_library/{user}'
    songs = []
    for dirs in os.listdir(default):
        for trck in os.listdir(f'{default}/{dirs}'):
            if trck[-3:] == 'mp3':

                song = {
                    'directory': f'{user}/{dirs}/{trck}',
                    'title': trck
                }
                
                songs.append(song)
                print(trck)
    print(songs)
    return render_template('plyaer.html', songs=songs)
