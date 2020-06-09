#******************************************************************************
# Insert licence here!



#******************************************************************************

from PySide2.QtGui import QIcon, QTextDocument
from PySide2.QtWidgets import QTreeWidgetItem

#******************************************************************************

class TaskItem (QTreeWidgetItem):

    """
     

    :version:
    :author:
    """

    #--------------------------------------------------------------------------
    
    def __init(self):
        super.__init__()
        
        # Define attributes
        self.note = QTextDocument()
        self.deadline  = 0
           
    #--------------------------------------------------------------------------



