import xml.etree.ElementTree as ET
from xml.dom import minidom

def  correctform(type):
    stringET = ET.tostring(type, encoding='unicode', method='xml')
    new =minidom.parseString(stringET)
    return new.toprettyxml(indent="     ", newl="\n")

root = ET.Element('Root')
ET.SubElement(root,'node', icon='1', expanded='true')
ET.SubElement(root[0],'title')
ET.SubElement(root[0],'note')
ET.SubElement(root[0],'deadline')
ET.SubElement(root[0],'node', icon='2', expanded='true')
ET.SubElement(root[0][3],'title')
ET.SubElement(root[0][3],'note')
ET.SubElement(root[0][3],'deadline')
ET.SubElement(root,'node', icon='3', expanded='false')
ET.SubElement(root[1],'title')
ET.SubElement(root[1],'note')
ET.SubElement(root[1],'deadline')

root[0][0].text="Reminder"
root[0][1].text="Don't forget me this weekend!"
root[0][2].text="20200520T1300"

root[0][3][0].text="child"
root[0][3][1].text="another reminder!"
root[0][3][2].text="20200521T1430"

root[1][0].text="Reminder2"
root[1][1].text="Don't forget me this weekend!"
root[1][2].text="20200522T1600"

myfile = open("tree.xml", "w+")
mynode =  correctform(root)
myfile.write( mynode )