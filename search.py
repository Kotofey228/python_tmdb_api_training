import json_serializer


if __name__ == '__main__':
    keyword = input('Введите ключевое слово: ')
    collection = json_serializer.get_decoded_json('collection')

    title_list = []
    for title in collection.keys():
        if keyword.lower() in title.lower().split():
            title_list.append(title)

    print('\nРезультаты:\n')
    for title in title_list:
        print(title)
