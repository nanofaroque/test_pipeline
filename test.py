def file_write_omar(data):
    file = open('testfile.json', 'a')
    file.write(''.join(str(data)))


omar_dict = {'name': 'Omar',
             'age': 33,
             'children': 'Eshika'
             }
file_write_omar(omar_dict)


def test():
    with open('sample.xml', 'r') as f, open('new_sample.xml', 'w') as g:
        g.write('<dependencies>{}</dependencies>'.format(f.read()))

        import xml.etree.ElementTree as ET
        tree = ET.parse('new_sample.xml')
        root = tree.getroot()
        # print(root)
