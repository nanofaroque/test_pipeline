import json
def file_write():
    file = open('testfile.txt', 'a')
    person_dict = {'name': 'Bob',
                    'age': 12,
                    'children': None
                    }
    person_json = json.dumps(person_dict)
    file.write(''.join(str(person_dict)))

file_write()
