import xml.dom

try:
    f= open("sam1.xml", "w")
except IOError:
    f= open("sam1.xml", "w")
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write("<tree_save>")
    f.write("   <tree>")
    f.write("   </tree>")
    f.write("</tree_save>")



def create_tree(num):
 Document.getElementsByTagName('tree')[0].setAttribute("num" , num)

def add_Icon(icon):
    newEle = Document.createElement("Icon")
    newIcon = Document.createTextNode(icon)
    newEle.appendChild(newIcon)
    Document.getElementsByTagName("title")[0].appendChild(newEle)

def create_type():
    newElement = Document.createElement("title")
    Document.getElementsByTagName("tree")[1].appendChild(newElement)
    newElement = Document.createElement("note")
    Document.getElementsByTagName("tree")[2].appendChild(newElement)

def add_Deadline(deadline):
    newEle = Document.createElement("deadline")
    newline = Document.createTextNode(deadline)
    newEle.appendChild(newline)
    Document.getElementsByTagName("title")[4].appendChild(newEle)

create_tree(1)
create_type()

