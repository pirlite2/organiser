import xml.etree.ElementTree as ET
from xml.dom import minidom

root =ET.Element('Tree')

def  correctform(type):
    stringET = ET.tostring(type, encoding='unicode',method='xml')
    new =minidom.parseString(stringET)
    return new.toprettyxml(indent="     ", newl="\n")

def __init__(self):
    self.num={1,2,3}
    self.icon=""
    self.title = ""
    self.note = ""
    self.deadline = ""
    self.extened = ""

def first_node(self)
    for i in self.num:
        attribute= {'icon', self.icon}
        node[i] = ET.subElement(root[i],'node',attribute)
        ET.SubElement(node[id],'extened')
        node[i][0].text= self.extened
        ET.SubElement(node[i],'title')
        node[i][1].text= self.title
        ET.SubElement(node[i],'note')
        node[i][2].text= self.note 
        ET.SubElement(node[i],'deadline')
        node[i][3].text= self.deadline
def  save_xml(self):    
    for i in self.num:
        attribute= {'icon', self.icon}
        node[i*4] = ET.subElement(root[i*4],'node',attribute)
        ET.SubElement(node[i*4],'extened')
        node[i*4][0].text= self.extened
        ET.SubElement(node[i*4],'title')
        node[i*4][1].text= self.title
        ET.SubElement(node[i*4],'note')
        node[i*4][2].text= self.note 
        ET.SubElement(node[i*4],'deadline')
        node[i*4][3].text= self.deadline



myfile = open("tree.xml", "w+")
mynode =  correctform(root)
myfile.write( mynode )