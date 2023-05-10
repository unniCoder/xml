import xml.etree.ElementTree as ET

# Load the file
tree = ET.parse('CompRegulator.xml')
root = tree.getroot()
element=['Sections', 'FlgNet', ]
# Iterate over the elements
for elem in root.iter():
    if '}' in elem.tag:
        if elem.tag.split('}', 1)[1] not in element:
            elem.tag = elem.tag.split('}', 1)[1]
            #print(elem.tag)
    for name, value in list(elem.attrib.items()):
        print(name,value)
        #if '}' in name:
           # del elem.attrib[name]
           # elem.attrib[str(name).split('}', 1)[1]] = value
            
tree.write('CompRegulator2.xml', encoding='utf-8', xml_declaration=True  )   