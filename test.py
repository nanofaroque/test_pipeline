import json
def file_write():
    file = open('testfile.json', 'a')
    person_dict = {'name': 'Bob',
                    'age': 12,
                    'children': None
                    }
    #person_json = json.dumps(person_dict)
    file.write(''.join(str(person_dict)))

file_write()

def file_write_omar(data):
    file = open('testfile.json', 'a')
    #person_json = json.dumps(data)
    file.write(''.join(str(data)))

omar_dict = {'name': 'Omar',
                'age': 33,
                'children': 'Eshika'
                }
file_write_omar(omar_dict)
