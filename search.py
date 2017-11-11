import json

print('Введите ключевое слово:')
keyword = input()

encoded_coll = open('collection.json')
collection = json.load(encoded_coll)
encoded_coll.close()

title_list = []
for title in collection.keys():
    if keyword.lower() in title.lower().split():
        title_list.append(title)

for title in title_list:
    print(title)
