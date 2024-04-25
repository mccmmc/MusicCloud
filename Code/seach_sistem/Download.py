import mutagen.id3
import urllib.request
import yandex_music.exceptions
import os


def set_image(track, path):
    image_file = urllib.request.urlopen(track['image_link']).read()
    audio = mutagen.id3.ID3()
    audio.save(path)
    audio = mutagen.id3.ID3(path)
    audio.add(mutagen.id3.APIC(3, 'image/png', 3, 'uCover', image_file))
    return audio


def download_track(track, user):  # track downloader
    # path = set_path(client, path) / f"{track['title']}_{track['id']}.mp3"  # path to downloaded files

    print('trck', track)
    print(os.getcwd())
    os.mkdir(os.path.join(f'../static/music_library/{user}', track['id']))
    path = f'../static/music_library/{user}/{track["id"]}/track.mp3'
    print(path)
    track['track'].download(path)  # track download
    audio = set_image(track, path)  # add track image
    audio.add(mutagen.id3.TIT2(text=f"{track['title']}"))  # add track title
    audio.add(mutagen.id3.TALB(text=f"{', '.join(track['album'])}"))  # add track album
    audio.add(mutagen.id3.TCON(text=f"{', '.join(track['genre'])}"))  # add track genre
    audio.add(mutagen.id3.TPE1(text=f"{', '.join(track['author'])}"))  # add track artists
    audio.add(mutagen.id3.TYE(text=f"{', '.join(track['year'])}"))  # add track data
    audio.save(v2_version=3)
