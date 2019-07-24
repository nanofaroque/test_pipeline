def file_write(input_str):
    file = open('testfile.txt', 'a')

    person_dict = {'name': 'Bob',
                    'age': 12,
                    'children': None
                    }
                    person_json = json.dumps(person_dict)
    file.write(person_dict)
