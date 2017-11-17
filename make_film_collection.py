from sys import stdout

import tmdb
import json_serializer


def get_movie_collection(collection_len, api, year):
    movie_collecton = {}
    for page in range(1, 51):
        current_collection = tmdb.make_tmdb_api_request(
            method='/discover/movie',
            api_key=api,
            extra_params={'primary_release_year': int(year), 'page': page})['results']

        for film_num in range(len(current_collection)):
            movie_collecton.update(
                {current_collection[film_num]['title']: current_collection[film_num]})
            counter(len(movie_collecton), collection_len)
            if len(movie_collecton) == collection_len:
                break
    return movie_collecton


def counter(num, maxNum):
    stdout.write("\r%d" % num + '|' + str(maxNum))
    stdout.flush()


COLLECTION_LEN = 1000
if __name__ == '__main__':
    try:
        year = input('Введите год (1935-2017): ')
        if not(1934 <= int(year) <= 2017):
            raise ValueError
    except ValueError:
        print('Вы ввели неправильное значение, попробуйте снова.')
        exit()
    api_key = input('Введите ключ api: ')

    movies = get_movie_collection(COLLECTION_LEN, api_key, year)

    json_serializer.encode_json('collection', movies)

    print('\nГотово!')
