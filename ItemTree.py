#******************************************************************************
# Insert licence here!


#******************************************************************************

import os

from PySide2.QtGui import QIcon, QFont, QTextDocument
from PySide2.QtWidgets import QTreeWidget, QAbstractItemView, QDialog

from TaskItem import TaskItem
from NoteEditor import NoteEditor
from SetPreferences import SetPreferences

#******************************************************************************

class ItemTree (QTreeWidget):
    """
     Container for TaskItem instances 
    :version:
    :author: pir
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

        self.itemClicked.connect(self.on_item_clicked)
        self.itemDoubleClicked.connect(self.on_item_double_clicked)
       
        # Load tree icons from ./treeIcons directory
        self.treeIconsFilesList = os.listdir("./treeIcons")
        self.treeIconsFilesList.sort()
        self.treeIconsList = []
        for i in range(0, len(self.treeIconsFilesList)):
            self.treeIconsList.append(QIcon("./treeIcons/" + self.treeIconsFilesList[i]))
                                                    
        # Configure text edit class
        self.editBox = NoteEditor()
    
        # Default parameters
        self.defaultIconIndex = 0
        self.defaultTreeFont = QFont("Helvetica", 11)
        self.defaultTreeFontSize = 11
        
        return
        
    #--------------------------------------------------------------------------

    def insert_task_item(self, iconIndex, title, deadline, expanded, child):
        """
        Insert a new task item into the task tree with the supplied properties:
        
        iconIndex : index into treeIconsList specifying icon to be used for the node
        title: string of text used in tree
        deadline: int in ISO-8601 format of: YYYYMMDDHHMM
        expanded : True|False depending whether the node is to be expanded ot not
        child : True|False, depending on whether the task to be added is a child or not

        @return: None
        @author: pir
        """     
      
        if (self.topLevelItemCount() == 0):
            print("empty ItemTree instance")
            newTaskItem = TaskItem(self)
            self.setCurrentItem(newTaskItem, 0)
        else:
            print("container is not empty!")
            currentItem = self.currentItem()
            print(self.currentItem().text(0))   #test
            if (child == True):
                # Create child item
                newTaskItem = TaskItem(currentItem)
            else:
                # Create successor item
                print("creating successor item")    #test
                parentItem = currentItem.parent()
                print("type = ", type(parentItem))  #test 
                if (parentItem is None):
                    # Insert top level item
                    index = self.indexOfTopLevelItem(currentItem)
                    newTaskItem = TaskItem()
                    self.insertTopLevelItem(index + 1, newTaskItem)
                else:
                    newTaskItem = TaskItem(parentItem)

        # Add TaskItem to tree widget
        newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
        newTaskItem.setText(0, title)
        newTaskItem.note = QTextDocument()
        newTaskItem.deadline = deadline        
        newTaskItem.setExpanded(expanded)
        
        return
    
    #--------------------------------------------------------------------------

    def delete_task_item(self):
        """
        Delete the currently-selected task item from the task tree
        @return: None
        @author: 
        """

        targetItem = self.currentItem()
        # TODO
        
        return

    #--------------------------------------------------------------------------

    def add_task_item(self, iconIndex, title, note, deadline, expanded, indentLevel):
        """
        
        indentLevel: 0 = top-level item
        @return: None
        @author: 
        """
        
        # Add top level item
        newTaskItem = TaskItem(self)
        newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
        newTaskItem.setText(0, title)
        newTaskItem.note = QTextDocument()
        newTaskItem.deadline = deadline        
        newTaskItem.setExpanded(expanded)

        return

    #--------------------------------------------------------------------------


    def edit_task_item(self):
        """
        Edit the current selected task item
        @return:
        @author:
        """

        return

    #--------------------------------------------------------------------------
    
    def show_schedule(self):
        """
        Show the schedules for all items with assigned deadlines; ignore tasks without deadlines
        @return:
        @author:
        """

        return
    
    #--------------------------------------------------------------------------
        
    def search_tree(self):
        """  
        Search tree for specified text in title
        @return:
        @author:
        """

        return
    
    #--------------------------------------------------------------------------

    def search_notes(self):
        """
        Search notes for specified text
        @return:
        @author:
        """

        return

    #--------------------------------------------------------------------------
   
    def set_item_tree_preferences(self):
        """
        @return: None
        @author: pir
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
            print("rejected")
            
        # Update itemTree settings - TODO
                    
        return
        
    #--------------------------------------------------------------------------

    def on_item_clicked(self, currentItem, column):
        """
        Update text editor with note (QTextDocument) of current item
        @return: None
        @author: pir
        """
        print(currentItem.text(0), "task clicked") #test
        self.editBox.setDocument(currentItem.note)

        return

    #--------------------------------------------------------------------------

    def on_item_double_clicked(self, currentItem, column):
        """
        Edit properties of current item 
        @return:
        @author:
        """

        print(currentItem.text(0), "task double-clicked")   # test

        return
    
    #--------------------------------------------------------------------------


