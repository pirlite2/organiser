import xml.sax
class readHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.node=""
        self.title = ""
        self.note = ""
        self.deadline = ""

    def startElement( self, type, attributes):
        self.CurrentData =  type
        if  type == "node":
            print ('--- Node ---')
            Icon = attributes["icon"]
            print ("[", Icon, "]")
            Expanded = attributes["expanded"]
            if Expanded == 'true':
                print ('Expanded')
            else :
                print ('Compressed')


    def endElement( self, type):
        if self.CurrentData ==  "title":
            print ( 'Title: ',  self.title)
        elif self.CurrentData ==  "note":
            print ( 'Note: ', self.note)
        elif  self.CurrentData ==  "deadline":
            print ('Deadline:',  self.deadline)
        if  type == "node":
            print ('--- endNode ---')
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "note":
            self.note = content
        elif self.CurrentData == "deadline":
            self.deadline = content

if (__name__ =="__main__"):
    parser=xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler =  readHandler()
    parser.setContentHandler(Handler)
    parser.parse("/home/chingtung/文件/organiser-master/initial-xml-sketch.xml")