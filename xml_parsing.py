
import xml.etree.ElementTree as ET
tree = ET.parse('xml_parser.xml')
root = tree.getroot()
# root = ET.fromstring(country_data_as_string)
print root.tag
# print root.attrib
# for child in root:
# 	print child.tag, child.attrib


for country in root.findall('country'):
	rank = country.find('rank').text
	name = country.get('name')
	print name, rank