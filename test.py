import json
import xml.etree.ElementTree as ET


def file_write(data):
    file = open('testfile.json', 'a')
    file.write(''.join(str(data)))


def adding_extra_field_and_tag():
    with open('sample.xml', 'r') as f, open('new_sample.xml', 'w') as g:
        g.write('<?xml version="1.0"?>')
        g.write('<dependencies>{}</dependencies>'.format(f.read()))


adding_extra_field_and_tag()

tree = ET.parse('new_sample.xml')
root = tree.getroot()
dependencies = []
for child in root:
    v = None
    gId = str(child.find('groupId').text)
    aId = str(child.find('artifactId').text)
    if child.find('version') is not None:
        v = str(child.find('version').text)
    else:
        v = ''
    d = {'u_group': gId, 'u_artifact': aId, 'version': v}
    dependencies.append(json.dumps(d))
dd = json.dumps(dependencies)
file_write(dd)
