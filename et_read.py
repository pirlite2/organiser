import xml.etree.ElementTree as ET
from xml.dom import minidom

def  correctform(type):
    stringET = ET.tostring(type, encoding='unicode',method='xml')
    new =minidom.parseString(stringET)
    return new.toprettyxml(indent="     ", newl="\n")

node = ET.Element('node', icon = '1')
ET.SubElement(node,'extened')
ET.SubElement(node,'title')
ET.SubElement(node,'note')
ET.SubElement(node,'deadline')
ET.SubElement(node,'node')
ET.SubElement(node[4],'title')
ET.SubElement(node[4],'note')
ET.SubElement(node[4],'deadline')

node[0].text="ture"
node[1].text="Reminder"
node[2].text="Don't forget me this weekend!"
node[3].text="20200520T1300"
node[4][0].text="child"
node[4][1].text="another reminder!"
node[4][2].text="20200521T1430"

myfile = open("tree.xml", "w+")
mynode =  correctform(node)
myfile.write( mynode )