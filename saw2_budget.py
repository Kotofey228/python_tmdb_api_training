import tmdb


if __name__ == '__main__':
    api = input('Введите API: ')
    movie_info = tmdb.make_tmdb_api_request(method='/movie/215', api_key=api)
    print('{}$'.format(movie_info['budget']))
