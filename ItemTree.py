#******************************************************************************
# Insert licence here!

from PySide2.QtGui import QIcon, QFont
from PySide2.QtWidgets import QTreeWidget, QAbstractItemView

#******************************************************************************

from TaskItem import *
from NoteEditor import *
from SetPreferences import *

#******************************************************************************

class ItemTree (QTreeWidget):
    """
     Container for TaskItem instances
     
    :version:
    :author:
    """

    def __init__(self):
        super().__init__()
        
        # Configure tree widget
        self.setHeaderHidden(True)
        self.setColumnCount(2)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        
        #self.setColumnWidth(1,100)
        self.resizeColumnToContents(1)
        # how to set column widths to display string of arbitrary length????
        
        # Load tree icons... TODO
        self.treeIconsList = []
        self.treeIconsList.append(QIcon("./treeIcons/Gnome-folder-new.svg"))
                                                      
        # Configure text edit class
        self.editBox = NoteEditor()
    
        # Default parameters
        self.defaultIconIndex = 0
        self.defaultTreeFont = QFont("Times", 11)
        self.defaultTreeFontSize = 11
        
        return
        
    #--------------------------------------------------------------------------

    def add_task_item(self, iconIndex, title, note, deadline, expanded, child):
        """
        Add a task item to the task tree with the supplied properties

        @return  :
        @author
        """     
      
        # Add TaskItem to treeWidget
        newTaskItem = TaskItem(self)
        newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
        newTaskItem.setText(0, title)
        #newTaskItem.note = # set note text - TODO
        newTaskItem.deadline = deadline        
        newTaskItem.setExpanded(expanded)
        
        return
    
    #--------------------------------------------------------------------------

    def delete_task_item(self):
        """
         Delete the currently-selected task item to the task tree

        @return  :
        @author
        """
        
        
        return

    #--------------------------------------------------------------------------

    def edit_task_item(self):
        """
         

        @return  :
        @author
        """
        return

    #--------------------------------------------------------------------------
    
    def show_schedule(self):
        """
        
        @return  :
        @author
        """
        return
        
    #--------------------------------------------------------------------------
        
    def search_tree(self):
        """   

        @return  :
        @author
        """
        return
    
    #--------------------------------------------------------------------------

    def search_notes(self):
        """

        @return  :
        @author
        """
        return

    #--------------------------------------------------------------------------
   
    def set_item_tree_preferences(self):
        """

        @return  :
        @author
        """
                             
        preferenceDialog = SetPreferences()       
        preferenceDialog.set_tree_defaults(self.defaultTreeFont, self.defaultTreeFontSize, self.defaultIconIndex)
        if(preferenceDialog.exec_() == QDialog.Accepted):
			# Update tree parameters
            print("accepted")
           
            (self.defaultTreeFont, self.defaultTreeFontSize, self.defaultIconIndex) = preferenceDialog.get_tree_defaults()
            
            # test
            print("font = ", self.defaultTreeFont)
            print("font size = ", self.defaultTreeFontSize)
            print("default icon index = ", self.defaultIconIndex)
            # test
        else:
            print ("rejected")
                    
        return
        
    #--------------------------------------------------------------------------


