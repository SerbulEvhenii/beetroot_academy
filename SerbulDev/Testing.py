import xml.etree.ElementTree as ET
from lxml import etree


with open('17.1_part.xml', 'r') as doc_file:
    line1 = doc_file.readline()
    line2 = doc_file.readline()
    line3 = doc_file.readline()


import xml.etree.ElementTree as ET
tree = ET.parse('test_original.xml')
root = tree.getroot()
for child in root:
    print (child.tag, child.attrib)
print(root[0][0].text)

for neighbor in root.iter('STAN'):
    print(neighbor.text)





# print(line3)
# tree = etree.parse('17.1_part.xml')
# path = '17.1_part.xml'
# tree = etree.parse(path)
# root = tree.getroot()
#
# from lxml import etree
# xmlstring = '<EDRPOU>32034245</EDRPOU>'
# parser = etree.XMLParser(recover=True)
# root = etree.fromstring(xmlstring, parser=parser)
# print(root.tag)
# print(str(etree.tostring(root)))
#
# for element in root.iter("*"):
#     if element.text is not None and not element.text.strip():
#         element.text = None
#
# print(etree.tostring(root))
#

# parser = etree.XMLParser(encoding="utf-8")
# tree = etree.fromstring(xmlstring, parser=parser)