import jsonio

if __name__ == '__main__':
    coll = jsonio.get_decoded_json('collection')
    print(coll.keys())
