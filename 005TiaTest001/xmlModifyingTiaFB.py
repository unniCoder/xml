import xml.etree.cElementTree  as ET

ns = "" 
mytree = ET.parse('CompRegulator.xml')
myroot = mytree.getroot()
ET.register_namespace("1ns0", "http://www.siemens.com/automation/Openness/SW/Interface/v5")
ET.register_namespace("1ns1", "http://www.siemens.com/automation/Openness/SW/NetworkSource/FlgNet/v4")

#iterating through the price values.

#print(myroot.tag) # Document
#print(myroot[1])
def saveFile(fileName):
    # Remove namespace prefixes from element tags and attribute names
    for elem in myroot.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]
        for name, value in list(elem.attrib.items()):
            if '}' in name:
                del elem.attrib[name]
                elem.attrib[str(name).split('}', 1)[1]] = value
    
    ET.ElementTree(myroot).write(fileName + '.xml',xml_declaration=True,encoding='utf-8',default_namespace="")

def replaceInInterface(interface, oldvalue,newvalue):
    for child in myroot.iter('SW.Blocks.FB'):
        for state in child[0]: # navigate to block interface
            for step in state.iter('Interface'):
                for stat in step[0]:# navigate to interface units
                    for key0,value0 in stat.items():
                        if value0 == interface:
                            for tep in stat:
                                attrib_value = tep.attrib
                                #tep.attrib['Name']='value' #add new attrib
                                for key, value in attrib_value.items():
                                    if value == oldvalue:
                                        tep.attrib[key]=newvalue
    
    
    saveFile('CompTest')
            
def addInInterface():
    for child in myroot.iter('SW.Blocks.FB'):
        for state in child[0]: # navigate to block interface
            for step in state.iter('Interface'):
                for stat in step[0]:# navigate to interface units
                    for key0,value0 in stat.items():
                        if value0 == 'InOut':
                            for tep in stat:
                                attrib_value = tep.attrib
                                for key, value in attrib_value.items():
                                    if value == 'status':
                                        new_elem = ET.Element(tep.tag, tep.attrib)
                                        new_elem.extend(list(tep))
                                        stat[0].insert(2,new_elem)
                                        

                                        #tep.attrib[key]=newvalue


    with open('CompRegulator.xml', 'wb') as f:
        # Write the modified ElementTree object to the file
        for elem in myroot.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
            for name, value in list(elem.attrib.items()):
                if '}' in name:
                    del elem.attrib[name]
                    elem.attrib[str(name).split('}', 1)[1]] = value
        mytree.write(f, encoding='utf-8', xml_declaration=True  )                      

#replaceInInterface('InOut','status','value')
addInInterface()
#print(name) 


'''
for prices in myroot.iter('price'):
    # update the price value
    prices.text = str(float(prices.text)+10)
    # creates a new attribute
    prices.set('newprices', 'yes')

#creating a new tag under the parent.
#myroot[0] here is the first food tag
#ET.SubElement(myroot[1], 'tasty')
#for temp in myroot.iter('tasty'):
    #giving the value as Yes.
#    temp.text= str('YES')

#deleting attributes in the xml.
#by using the popu as attrib returns dictionary
#removes the itemid attribute in the name tag of
#the second food tag
#myroot[1][0].attrib.pop('itemid')

#removing the tag completely we use remove function.
#completely removes the third food tag.
print(myroot.tag)

#myroot.remove(myroot[2])

#mytree.write('output.xml')
'''