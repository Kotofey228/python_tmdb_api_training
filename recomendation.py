import json_serializer


def make_recomend_set(title):
    collection = json_serializer.get_decoded_json('collection')

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

    return recommendation_list


if __name__ == '__main__':
    title = input('Введите название фильма: ')

    recommend_list = make_recomend_set(title)

    print('\nРекомендованные:\n')
    for film in recommend_list:
        print(film)
