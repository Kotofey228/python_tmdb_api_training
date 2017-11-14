import tmdb


if __name__ == '__main__':
    movie_info = tmdb.make_tmdb_api_request(
        method='/movie/215', api_key=tmdb.api)
    print(str(movie_info['budget']) + '$')
