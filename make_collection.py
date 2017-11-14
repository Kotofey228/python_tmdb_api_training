import time
from sys import stdout

import tmdb
import jsonio


def get_movie_collection(coll_len, api, year):
    movie_collecton = {}
    page = 1
    while len(movie_collecton) < coll_len:
        current_coll = tmdb.make_tmdb_api_request(
            method='/discover/movie',
            api_key=api,
            extra_params={'primary_release_year': int(year), 'page': page})['results']

        for film_num in range(len(current_coll)):
            movie_collecton.update(
                {current_coll[film_num]['title']: current_coll[film_num]})
            counter(len(movie_collecton), coll_len)
            if len(movie_collecton) == coll_len:
                break
        page += 1
        print()
    return movie_collecton


def counter(num, maxNum):
    stdout.write("\r%d" % num + '|' + str(maxNum))
    stdout.flush()
    time.sleep(SLEEP_TIME)


SLEEP_TIME = 0.01
COLLECTION_LEN = 1000
if __name__ == '__main__':
    print('Введите год:')
    year = input()
    print('Введите ключ api')
    api_key = input()

    movies = get_movie_collection(COLLECTION_LEN, api_key, year)

    jsonio.encode_json('collection', movies)

    print('Готово!')
