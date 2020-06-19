import xml.etree.ElementTree as ET
from xml.dom import minidom



# set the XML files as a correct format
def  correctform(type):
        stringET = ET.tostring(type, encoding='unicode',method='xml')
        new = minidom.parseString(stringET)
        return new.toprettyxml(indent="     ", newl="\n") 

class data():   
    def __init__(self, item):
        self.icon= item.icon
        self.title = item.title
        self.note = item.note
        self.deadline = item.deadline
        self.expanded = item.expanded

    def add_node(self,target):

        if  target == tree:
            path = ET.SubElement(tree,'task', icon=self.icon, expanded=self.expanded)
            ET.SubElement(path,'title')
            path[0].text= self.title
            ET.SubElement(path,'note')
            path[1].text= self.note 
            ET.SubElement(path,'deadline')
        else:
            path = ET.SubElement(target,'task', icon=self.icon, expanded=self.expanded)
            ET.SubElement(path,'title')
            path[0].text= self.title
            ET.SubElement(path,'note')
            path[1].text= self.note 
            ET.SubElement(path,'deadline')
            path[2].text= self.deadline
        return path

def roll_whole_tree(parent):
    j=0
    child_count = parent.childCount()
    for i in range(child_count):
        item = parent.child(i)
        write=data(item)
        target[j+1]=write.add_node(target[j])
        if item.nodetype == 'folder':
            j=j+1
            roll_whole_tree(item)
            j=j-1

