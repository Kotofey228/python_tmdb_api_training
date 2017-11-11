import json

print('Введите название фильма:')
title = input()

encoded_coll = open('collection.json')
collection = json.load(encoded_coll)
encoded_coll.close()
if title in collection.keys():
    film = collection[title]
else:
    print('Фильм не найден')
    exit()
genres = film['genre_ids']

recommendation_list = set()

for film in collection:
    if film == title:
        continue
    for g in genres:
        if g in collection[film]['genre_ids']:
            recommendation_list |= set([film])
    if len(recommendation_list) > 10:
        break

print('Рекомендованные:')
for film in recommendation_list:
	print(film)