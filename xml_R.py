import xml.sax
class readHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.root=""
        self.node=""
        self.title = ""
        self.note = ""
        self.deadline = ""
        
    def startElement( self, type, attributes):
        self.CurrentData =  type
        if  type == "tree":
            print('***Tree***')
        if type=="task":
            Icon = attributes["icon"]
            print ('--- Task ---')
            print('Icon:',Icon)
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
        if  type == "task":
            print ('---endtask---')
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "note":
            self.note = content
        elif self.CurrentData == "deadline":
            self.deadline = content
