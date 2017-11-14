import jsonio

print('Введите ключевое слово:')
keyword = input()
print()
collection = jsonio.get_decoded_json('collection')

title_list = []
for title in collection.keys():
    if keyword.lower() in title.lower().split():
        title_list.append(title)

for title in title_list:
    print(title)
