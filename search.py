import tmdb
import json
from pprint import pprint
import time
from sys import stdout

print('Введите ключевое слово:')
keyword = input();

encoded_coll = open('collection.json')
collection = json.load(encoded_coll)
encoded_coll.close()

title_list = []
for title in collection:
	if title.lower().find(keyword.lower()):title_list.append(title)

for title in title_list:
	print(title)