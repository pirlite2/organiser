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
        
    def attributes(self, deadline, icon):
        # Define attributes
        self.note = QTextDocument()
        self.deadline  = deadline
        self.icon = icon
        
        return
           
    #--------------------------------------------------------------------------



