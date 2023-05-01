import xml.etree.ElementTree as ET
XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
<States>
    <state name ="TELANGANA">
        <rank>1</rank>
        <neighbor name ="ANDHRA" language ="Telugu"/>
        <neighbor name ="KARNATAKA" language ="Kannada"/>
    </state>
    <state name ="GUJARAT">
        <rank>2</rank>
        <neighbor name ="RAJASTHAN" direction ="N"/>
        <neighbor name ="MADHYA PRADESH" direction ="E"/>
    </state>
    <state name ="KERALA">
        <rank>3</rank>
        <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
    </state>
</States>
'''
# parsing from the string.
root = ET.fromstring(XMLexample_stored_in_a_string)
#printing attributes of the root tags
for neighbor in root.iter('neighbor'):
    name = neighbor.get('name')
    print(neighbor.attrib, name)

#finding the state tag and their child attributes.
for state in root.findall('state'):
    rank = state.find('rank').text
    name = state.get('name')
    print(name, rank)
