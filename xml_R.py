import xml.sax
class readHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.root=""
        self.node=""
        self.title = ""
        self.note = ""
        self.deadline = ""
        self.extened = ""
        
    def startElement( self, type, attributes):
        self.CurrentData =  type
        if  type == "Root":
            print('***Root***')
        if type=="node":
            Icon = attributes["icon"]
            print ('--- Node',"[",Icon,"]",'---')
            Expanded = attributes["expanded"]
            if Expanded=="true":
                print('Expanded')
            elif Expanded=="false":
                print('Compressed')

    def endElement( self, type):  
        if self.CurrentData ==  "title":
            print ( 'Title:',self.title)
        elif self.CurrentData ==  "note":
            print ( 'Note:',self.note)
        elif  self.CurrentData ==  "deadline":
            print ('Deadline:',self.deadline)
        if  type == "node":
            print ('---endnode---')
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "extened":
            self.extened= content
        elif self.CurrentData == "title":
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
    parser.parse("tree.xml")