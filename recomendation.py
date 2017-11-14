import jsonio

print('Введите название фильма:')
title = input()

collection = jsonio.get_decoded_json('collection')
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
print()
for film in recommendation_list:
    print(film)
