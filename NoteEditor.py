#******************************************************************************
# Insert licence here!


#******************************************************************************

from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import QTextEdit

#******************************************************************************

class NoteEditor(QTextEdit):
    """ 
    :version:
    :author:
    """

    #--------------------------------------------------------------------------
    
    def __init__(self):
        super().__init__()
        
        return

    #--------------------------------------------------------------------------

    def setTextDocument(self, document):
        """
        Set document of text editor
        :version:
        :author:
        """

        self.setDocument(document)

        return

    #--------------------------------------------------------------------------