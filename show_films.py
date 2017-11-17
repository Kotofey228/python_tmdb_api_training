import json_serializer

if __name__ == '__main__':
    coll = json_serializer.get_decoded_json('collection')
    print(coll.keys())
