import json


def get_decoded_json(name):
    file = open(name + '.json')
    encoded_coll = json.load(file)
    file.close()
    return encoded_coll


def encode_json(name, dictionary):
    file = open('collection.json', 'w')
    json.dump(dictionary, file)
    file.close()
