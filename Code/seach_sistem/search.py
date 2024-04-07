import yandex_music.exceptions


def create_client(token):
    return yandex_music.Client(token).init()


def search_tracks(client, request):
    short_result = []
    try:
        search_result = client.search(request)
        try:
            for result in search_result['tracks']['results']:
                track = dict()
                track['id'] = str(result['id'])
                track['title'] = result['title']
                track['album'] = list(map(lambda x: x.title, result.albums))
                track['genre'] = list(map(lambda x: x.genre, result.albums))
                track['author'] = result.artists_name()
                track['year'] = list(map(lambda x: str(x.year), result.albums))
                track['image_link'] = result.get_cover_url('1000x1000')
                # track['image_bin_light'] = urllib.request.urlopen(result.get_cover_url('100x100')).read()
                # track['image_bin_huge'] = urllib.request.urlopen(result.get_cover_url('400x400')).read()
                track['track'] = result
                short_result.append(track)

            return short_result
        except TypeError:
            raise TypeError
    except yandex_music.exceptions.BadRequestError:
        return yandex_music.exceptions.BadRequestError


if __name__ == '__main__':
    user_token = 'AQAAAAAUjRFAAAG8Xn57pRR2lU7mqYicZyxhLlQ'
    req = input()
    cli = yandex_music.Client(user_token).init()
    print(search_tracks(cli, req))
