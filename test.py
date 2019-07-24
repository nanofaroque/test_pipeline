import json
def file_write_omar(data):
    file = open('testfile.json', 'a')
    #person_json = json.dumps(data)
    file.write(''.join(str(data)))

omar_dict = {'name': 'Omar',
            'age': 33,
            'children': 'Eshika'
                }
file_write_omar(omar_dict)
