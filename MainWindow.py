#! /usr/bin/python3

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

import sys
import os
from pathlib import Path

from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide2.QtWidgets import QMenuBar, QMenu, QAction
from PySide2.QtWidgets import QToolBar
#from PySide2.QtWidgets import QStatusBar
from PySide2.QtWidgets import QFileDialog
from PySide2.QtWidgets import QMessageBox

from ItemTree import *

#******************************************************************************

class MainWindow(QMainWindow):
    """
    Main application window
    :version:
    :author: pir, Hong Zhou
    """
   #--------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Organiser")
        self.mainLayout = QVBoxLayout()

        self.cwd = os.getcwd()  # Get the location of the current program file

        # Create menu bar & menus
        self.fileMenu = self.menuBar().addMenu("&File")
        self.openMenuAction = self.fileMenu.addAction("&Open")
        self.openMenuAction.triggered.connect(self.on_open_action)    # New-style connect!     
        self.saveMenuAction = self.fileMenu.addAction("&Save")
        self.saveMenuAction.triggered.connect(self.on_save_action)
        self.saveAsMenuAction = self.fileMenu.addAction("&Save as")
        self.saveAsMenuAction.triggered.connect(self.on_save_as_action)
        self.fileMenu.addSeparator()
        self.fileMenu.addSeparator()  
        self.fileMenu.addSeparator()
        self.quitMenuAction = self.fileMenu.addAction("&Quit")
        self.quitMenuAction.triggered.connect(self.on_quit_action)

        self.searchMenu = self.menuBar().addMenu("&Search")
        self.scheduleMenuAction = self.searchMenu.addAction("Show schedule") 
        self.scheduleMenuAction.triggered.connect(self.on_show_schedule_action)
        self.searchTreeMenuAction = self.searchMenu.addAction("Search tree") 
        self.searchTreeMenuAction.triggered.connect(self.on_search_tree_action)
        self.searchNotesMenuAction = self.searchMenu.addAction("Search notes") 
        self.searchNotesMenuAction.triggered.connect(self.on_search_notes_action)

        self.optionsMenu = self.menuBar().addMenu("&Options")
        self.showScheduleOnStartupAction = self.optionsMenu.addAction("Show schedule on startup")
        self.showScheduleOnStartupAction.setCheckable(True)

        self.setPreferencesMenuAction = self.optionsMenu.addAction("Set Preferences")
        self.setPreferencesMenuAction.triggered.connect(self.on_set_preferences_action)  

        self.aboutMenu = self.menuBar().addMenu("&About")
        self.aboutMenuAction = self.aboutMenu.addAction("&About") #record everybody's contributions
        self.aboutMenuAction.triggered.connect(self.on_about_action)
        
        # Create main toolbar
        self.mainToolBar = QToolBar()
        self.mainToolBar.setMovable(False)

        # Icons from https://commons.wikimedia.org/wiki/GNOME_Desktop_icons       
        self.addItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add.svg"), "Insert new item")
        self.addItemToolButton.triggered.connect(self.on_insert_item_action)      
        
        self.addChildItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add-child.svg"), "Insert child item")
        self.addChildItemToolButton.triggered.connect(self.on_insert_child_item_action)      
        
        self.deleteItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-delete.svg"), "Delete item")  
        self.deleteItemToolButton.triggered.connect(self.on_delete_item)
             
        self.mainLayout.addWidget(self.mainToolBar)

        # Configure window splitter
        self.splitter = QSplitter()
        self.splitter.setHandleWidth(2)

        # Configure item tree widget
        self.itemTree = ItemTree()  #find the itemtree
        self.splitter.addWidget(self.itemTree)      
        self.splitter.addWidget(self.itemTree.editBox)
        self.mainLayout.addWidget(self.splitter)

        # Is a status bar needed in this application?
        #self.statusBar = QStatusBar()
        #self.mainLayout.addWidget(self.statusBar)

        # Set layout as the central widget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

        # Parameters
        self.filePath = ""
        self.currentDirectory = str(Path.home())
        self.dirtyBit = False  # Indicates whether tree has been modified
        
        return
        
    #--------------------------------------------------------------------------
    
    def on_insert_item_action(self):
        """
        Handler for 'add item' action
        :version:
        :author: pir
        """
        
        isExpanded = True
        isChild = False
        self.itemTree.insert_task_item(isExpanded, isChild)
        self.dirtyBit = True

        return
        
   #--------------------------------------------------------------------------
   
    def on_insert_child_item_action(self):
        """
        Handler for 'add child item' action
        :version:
        :author: pir 
        """

        isExpanded = True
        isChild = True
        self.itemTree.insert_task_item(isExpanded, isChild)
        self.dirtyBit = True

        return
        
   #--------------------------------------------------------------------------

    def on_delete_item(self):
        """
        Handler for "Delete" action
        :version:
        :author: Sam Maher. pir 
        """

        # Check user really wants to delete the task
        # TODO


        self.itemTree.delete_task_item()
        self.dirtyBit = True

        return

    #--------------------------------------------------------------------------

    def on_edit_item(self):
        """
        Handler for edit task
        :version:
        :author: pir 
        """

        self.itemTree.edit_task_item()
        self.dirtyBit = True

        return

    #--------------------------------------------------------------------------

    def open_file(self, filePath):
        """
        :version:
        :author: ??? 
        """

        # Read XML file


        # call add_task_item() to build tree

        # test
        #f = open(self.filePath) # Read the file
        #lines = f.read()
        #print(lines)
        #f.close()
        # test 

        self.dirtyBit = False     

        return

    #--------------------------------------------------------------------------    

    def save_file(self, filePath):
        """
        :version:
        :author: ???
        """

        # Write XML file

        
        self.dirtyBit = False

        return

    #--------------------------------------------------------------------------
    
    def on_open_action(self):
        """
        Handler for 'File/Open' action
        :version:
        :author: Hong Zhou
        """

        # Get file path
        (filePath, filetype) = QFileDialog.getOpenFileName(self, "Open", self.currentDirectory, "Organiser file (*.xml);;Text Files (*.txt)")

        print("file = ", filePath) # debug

        if filePath != "":
            self.filePath = filePath
        else:
            return

        print("Opening: ", self.filePath)
             
        (path,fileName) = os.path.split(self.filePath)
        self.currentDirectory = path
        print("filename:", fileName)
        print("directory:", path)
        self.setWindowTitle("Organiser - " + fileName)
        
        self.open_file(self.filePath)
      
        return
        
    #--------------------------------------------------------------------------

    def on_save_action(self):
        """
        Handler for "File/Save" menu action
        :version:
        :author: Hong Zhou, pir
        """

        if self.filePath == "" :
            (filePath, fileType) = QFileDialog.getSaveFileName(self, "Save", self.currentDirectory, "Organiser file (*.xml)")

            if filePath != "":
                # Check entered pathname ends with ".xml"
                if not filePath.endswith(".xml"):
                    filePath += ".xml"      
                self.filePath = filePath
            else:
                return

        print("saving as", self.filePath)

        # Update main window title
        (path,fileName) = os.path.split(self.filePath)
        self.currentDirectory = path
        print("filename:", fileName)
        print("directory:", path)
        self.setWindowTitle("Organiser - " + fileName)

        self.save_file(self.filePath)

        return

    #--------------------------------------------------------------------------

    def on_save_as_action(self):
        """
        Handler for "File/Save as" menu action
        :version:
        :author: Hong Zhou, pir
        """
       
        (saveAsFilePath, savAsFileType) = QFileDialog.getSaveFileName(self, "Save as", self.currentDirectory, "Organiser file (*.xml)")
        
        if saveAsFilePath != "":
                # Check entered pathname ends with ".xml"
            if not saveAsFilePath.endswith(".xml"):
                    saveAsFilePath += ".xml"    
            self.filePath = saveAsFilePath
        else:
            return

        # Update main window title
        (path,fileName) = os.path.split(self.filePath)
        self.currentDirectory = path
        print("filename:", fileName)
        print("directory:", path)
        self.setWindowTitle("Organiser - " + fileName)

        self.save_file(self.filePath)

        return

    #--------------------------------------------------------------------------
    
    def on_quit_action(self):
        """
        Handler for 'File/Quit' menu action
        :version:
        :author: pir, Hong Zhou
        """

        # Check whether data needs to be auto-saved on exit
        if self.dirtyBit:
            self.save_file(self.filePath)

        print("quitting application")
        self.close()
        
        return

    #--------------------------------------------------------------------------

    def on_show_schedule_action(self):
        """
        Handler for 'Search/Schedule' menu action
        :version:
        :author: pir
        """

        return

    #--------------------------------------------------------------------------

    def on_search_tree_action(self):
        """
        Handler for 'Search/Search tree' menu action
        :version:
        :author: pir
        """

        return

    #--------------------------------------------------------------------------

    def on_search_notes_action(self):
        """
        Handler for 'Search/Search notes' menu action
        :version:
        :author: pir
        """

        return

    #--------------------------------------------------------------------------
      
    def on_set_preferences_action(self):
        """
        Handler for 'Options/Set preferences' menu action
        :version:
        :author: pir
        """        
        
        self.itemTree.set_item_tree_preferences()
        
        return
    
    #--------------------------------------------------------------------------   

    def on_about_action(self):
        """
        Handler for "About/About" action
        :version:
        :author: Hong Zhou
        """

        aboutMessage = "Tutor: Peter Rockett\nMainWindow: Hong Zhou\nInterface to XML: Chung Tung Ching\nSetPreferences: Yuqi Jin\nshow_schedule(), search_note() ＆ search_tree(): Tong Wang\nItemTree: Samuel Maher\nNoteEditor: Joseph-William Szetu\nSpell checker: Andrei Georgescu"
        QMessageBox.about(self, "Developer List", aboutMessage)

        return

#******************************************************************************

# Main program
if __name__ == "__main__":
    application = QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()

    # Load last file name at startup

    if mainWindow.showScheduleOnStartupAction.isChecked():
        mainWindow.itemTree.show_schedule()



    # test add_task_item()
    mainWindow.itemTree.add_task_item(0, "initial task from main()", "note1", 202006200000, True, 0)
    mainWindow.itemTree.add_task_item(0, "hello2", "note2", 202006220000, True, 0)
    mainWindow.itemTree.add_task_item(0, "first child", "note3", 202006210000, True, 0)
    # test



    exit(application.exec_())   # Not sure why this still has to be `exec_` with a trailing underscore?

#******************************************************************************
