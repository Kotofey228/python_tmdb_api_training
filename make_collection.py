import tmdb
import json

from pprint import pprint
import time

from sys import stdout

print('Введите год:')
year = input()
movie_collecton = {}
page = 1
while len(movie_collecton)<1000:
    current_coll = tmdb.make_tmdb_api_request(method='/discover/movie', api_key=tmdb.api, extra_params={'primary_release_year': int(year), 'page': page})
    for j in range(len(current_coll['results'])):
        movie_collecton.update({current_coll['results'][j]['title']: current_coll['results'][j]})
        stdout.write("\r%d" % len(movie_collecton) + '|1000')
        stdout.flush()
        if len(movie_collecton)==1000: break
    page+=1
collection = open('collection.json', 'w')
json.dump(movie_collecton, collection)
collection.close()

print('Готово!')
