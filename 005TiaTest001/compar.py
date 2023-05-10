import xml.etree.ElementTree as ET

# Load the first file
tree1 = ET.parse('CompRegulator.xml')
root1 = tree1.getroot()

# Load the second filecd 
tree2 = ET.parse('CompRegulator1.xml')
root2 = tree2.getroot()
list02= []
list01 = []
# Iterate over the elements in the first file
for elem1 in root1.iter():
    # Find the corresponding element in the second file
    list01.append((elem1.tag,elem1.attrib))

for elem2 in root2.iter():
    # Find the corresponding element in the second file
    list02.append((elem2.tag,elem2.attrib))
   
for x in range(len(list01)):
    if list01[x] !=list02[x]:
        print(list01[x], list02[x])
