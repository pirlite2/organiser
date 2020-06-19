#******************************************************************************
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA. 
#******************************************************************************

import os

from PySide2.QtGui import QIcon, QFont, QTextDocument, QColor
from PySide2.QtWidgets import QTreeWidget, QAbstractItemView, QDialog, QInputDialog, QTreeWidgetItem, QMessageBox

from TaskItem import TaskItem
from NoteEditor import NoteEditor
from SetPreferences import SetPreferences
from EditTaskItem import *

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

    def insert_task_item(self, expanded, child):
        """
        Insert a new task item into the task tree with the supplied properties:
        
        expanded : True|False depending whether the node is to be expanded ot not
        child : True|False, depending on whether the task to be added is a child or not

        @return: None
        @author: pir
        """     
      
        # Get task parameters
        title = ""
        deadline = 0
        editTaskDialog = EditTaskItem(self.defaultIconIndex, title, deadline, self.treeIconsList)
        if editTaskDialog.exec_() == QDialog.Accepted:
            (iconIndex, title, deadline) = editTaskDialog.get_item_values()
        else:
            return

        if self.topLevelItemCount() == 0:
            newTaskItem = TaskItem(self)
            self.setCurrentItem(newTaskItem, 0)
        else:
            currentItem = self.currentItem()
            if child == True:
                # Create child item
                newTaskItem = TaskItem(currentItem)
            else:
                # Create successor item
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
        newTaskItem.iconIndex = iconIndex
        newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
        newTaskItem.setText(0, title)
        newTaskItem.note = QTextDocument()
        newTaskItem.deadline = deadline        
        newTaskItem.setExpanded(expanded)

        # Give new item the focus
        self.setCurrentItem(newTaskItem, 0)
        self.editBox.setNoteDocument(newTaskItem.note)
        
        return
    
    #--------------------------------------------------------------------------

    def delete_task_item(self):
        """
        Delete the currently-selected task item from the task tree
        @return: None
        @author: Sam Maher
        """

        targetItem = self.currentItem()
        targetParent = targetItem.parent()
        index = self.indexOfTopLevelItem(targetItem)

        if (targetParent is None):
            self.takeTopLevelItem(index)
        else:
            targetParent.removeChild(targetItem)
        
        return

    #--------------------------------------------------------------------------

    def add_task_item(self, iconIndex, title, note, deadline, expanded, indentLevel):
        """
        Add tree items programmatically
                
        iconIndex : index into treeIconsList specifying icon to be used for the node
        title: string of text used in tree
        note: string to instanatiate note
        deadline: int in ISO-8601 format of: YYYYMMDDHHMM
        expanded : True|False depending whether the node is to be expanded ot not
        indentLevel: 0 = top-level item

        @return: None
        @author: pir, Sam Maher
        """
        myStack = []

        if self.topLevelItemCount() == 0:
            # Add first top level item
            assert indentLevel == 0, "First task must be at indent level 0"
            newTaskItem = TaskItem(self)
            newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
            newTaskItem.setText(0, title)
            newTaskItem.note = QTextDocument(note)
            newTaskItem.deadline = deadline        
            newTaskItem.setExpanded(expanded)
            myStack.append(newTaskItem)
        else:

            # Create Parent
            if indentLevel == 0:
                newTaskItem = TaskItem(self)
                newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
                newTaskItem.setText(0, title)
                newTaskItem.note = QTextDocument()
                newTaskItem.deadline = deadline        
                newTaskItem.setExpanded(expanded)
                myStack.append(newTaskItem)
            else:
                # Create Successor
                if indentLevel == myStack.pop().indentLevel:
                    newTaskItem = TaskItem(myStack.pop().parent)
                    newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
                    newTaskItem.setText(0, title)
                    newTaskItem.note = QTextDocument()
                    newTaskItem.deadline = deadline        
                    newTaskItem.setExpanded(expanded)
                    myStack.append(newTaskItem)
                # Create child
                else:
                    newTaskItem = TaskItem(myStack.pop())
                    newTaskItem.setIcon(0, self.treeIconsList[iconIndex])
                    newTaskItem.setText(0, title)
                    newTaskItem.note = QTextDocument()
                    newTaskItem.deadline = deadline        
                    newTaskItem.setExpanded(expanded)
                    myStack.append(newTaskItem)
        
        return

        

    #--------------------------------------------------------------------------

    def edit_task_item(self):
        """
        Edit the currently-selected task item
        @return:
        @author: Sam Maher
        """

        targetItem = self.currentItem()
        title = targetItem.text(0)
        deadline = targetItem.deadline
        editTaskDialog = EditTaskItem(self.defaultIconIndex, title, deadline, self.treeIconsList)
        if editTaskDialog.exec_() == QDialog.Accepted:
            (iconIndex, title, deadline) = editTaskDialog.get_item_values()
        else:
            return
  
        # Update target item properties
        targetItem.iconIndex = iconIndex
        targetItem.setIcon(0, self.treeIconsList[iconIndex])
        targetItem.setText(0, title)
        targetItem.deadline = deadline        

        return

    #--------------------------------------------------------------------------
    
    def show_schedule(self):
        """
        Show the schedules for all items with assigned deadlines; ignore tasks without deadlines
        @return:
        @author:Tong Wang
        """

        # get all notes with deadlines, put into a list
        notesList = []

        # go through the tree, collect notes with deadlines
        def iterateFunc(parent):
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)

                if item.nodetype == 'note' and item.deadline != 'none':
                    notesList.append(item)

                # if node type is folder，recursively call sub-items
                if item.nodetype == 'folder':
                    iterateFunc(item)

        root = self.invisibleRootItem()
        iterateFunc(root)

        # show actual schedule
        def bubbleSort(arr):
            length = len(arr)

            for j in range(length - 1, 0, -1):
                for i in range(0, length - 1):
                    if arr[i].deadline > arr[i + 1].deadline:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]

            return arr

        bubbleSort(notesList)
        #infoList = [f'   {item.deadline} {item.title}           ' for item in notesList]   # THIS LINE BREAKS THE CODE!!!!

        QMessageBox.information(self, 'Task Schedule', '\n'.join(infoList))

        return
    
    #--------------------------------------------------------------------------
        
    def search_tree(self):
        """  
        Search tree for specified text in title
        @return: None
        @author:Tong Wang
        """

        def searchFunc(parent):
            "Recursively calls the function to complete the search filtering of the entire tree"
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)
                if keywords in item.text(0):
                    item.setBackgroundColor(0, QColor('#c9e9e3'))
                else:
                    item.setBackgroundColor(0, QColor('white'))

                if item.nodetype == 'folder':
                    searchFunc(item)

        if keywords == '':
            keywords = '$%#$%@#$@#$@#$!!!$' # Make an impossible string in reality to make a mismatch
        root = self.invisibleRootItem()
        searchFunc(root)

        return
    
    #--------------------------------------------------------------------------

    def search_notes(self):
        """
        Search notes for specified text
        @return:
        @author:Tong Wang
        """

        te = self.ui.textEdit

        cursor = te.textCursor()

        # clear format
        cursor.select(QtGui.QTextCursor.Document)
        cursor.setCharFormat(QtGui.QTextCharFormat())
        cursor.clearSelection()
        te.setTextCursor(cursor)


        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("#6ac06e")))

        searchString = self.ui.keywords_2.text()
        # Empty string, empty selection
        if searchString == '':
            # Clear format
            cursor.select(QtGui.QTextCursor.Document)
            cursor.setCharFormat(QtGui.QTextCharFormat())
            cursor.clearSelection()
            te.setTextCursor(cursor)
            return

        # Process the displayed document
        pos = 0

        lenOfs = len(searchString)
        while True:
            index = te.toPlainText().find(searchString,pos)
            if index < 0:
                break

            cursor.setPosition(index)

            cursor.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.MoveMode.KeepAnchor, lenOfs)
            cursor.mergeCharFormat(format)

            pos = index + lenOfs

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

        self.editBox.setNoteDocument(currentItem.note)

        return

    #--------------------------------------------------------------------------

    def on_item_double_clicked(self, currentItem, column):
        """
        Edit properties of current item 
        @return:
        @author: pir
        """

        self.edit_task_item()

        return
    
#******************************************************************************
