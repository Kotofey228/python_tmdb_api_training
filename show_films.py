import json

c = open('collection.json')
coll = json.load(c)
c.close()
print(coll.keys())
