import xml.etree.ElementTree as ET


tree = ET.parse('document.xml')
root= tree.getroot()
XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
<COUNTRIES>
    <country name ="INDIA">
        <neighbor name ="Dubai" direction ="W"/>
    </country>
    <country name ="Singapore">
        <neighbor name ="Malaysia" direction ="N"/>
    </country>
</COUNTRIES>
'''

#Parsing using the string

stringroot= ET.fromstring(XMLexample_stored_in_a_string)

print (root)
print(stringroot)