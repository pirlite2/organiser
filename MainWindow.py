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

from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide2.QtWidgets import QMenuBar, QMenu, QAction
from PySide2.QtWidgets import QToolBar #, QInputDialog
#from PySide2.QtWidgets import QStatusBar   #Why make this line to comment? A: Because it's not needed
from PySide2.QtWidgets import QFileDialog

from PySide2.QtWidgets import QMessageBox

from ItemTree import *
from pathlib import Path
import xml_R
import ET_ADD
import xml.sax
#******************************************************************************

class MainWindow(QMainWindow):
    """
    Main application window
    :version:
    :author: pir & Hong Zhou
    """
   #--------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Organiser")
        self.mainLayout = QVBoxLayout()

        self.cwd = os.getcwd()  #Gets the location of the current program file

        # Create menu bar & menus
        self.fileMenu = self.menuBar().addMenu("&File")

        self.openMenuAction = self.fileMenu.addAction("&Open")
        self.openMenuAction.triggered.connect(self.on_open_action)    # New-style connect!
        
        self.saveMenuAction = self.fileMenu.addAction("&Save")
        self.saveMenuAction.triggered.connect(self.on_save_action)

        self.saveAsMenuAction = self.fileMenu.addAction("&Save as")
        self.saveAsMenuAction.triggered.connect(self.on_save_as_action)
        self.fileMenu.addSeparator()

        self.aboutMenuAction = self.fileMenu.addAction("&About") #record everybody's contributions
        self.aboutMenuAction.triggered.connect(self.on_about_action)
        self.fileMenu.addSeparator()

        self.setPreferencesMenuAction = self.fileMenu.addAction("Set Preferences")
        self.setPreferencesMenuAction.triggered.connect(self.on_set_preferences_action)        
        self.fileMenu.addSeparator()

        self.quitMenuAction = self.fileMenu.addAction("&Quit")
        self.quitMenuAction.triggered.connect(self.on_quit_action)
        
        # Create main toolbar
        self.mainToolBar = QToolBar()
        self.mainToolBar.setMovable(False)
        
        self.addItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add.svg"), "Insert new item")  # Icons from https://commons.wikimedia.org/wiki/GNOME_Desktop_icons
        self.addItemToolButton.triggered.connect(self.on_insert_item_action)      
        
        self.addChildItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-add-child.svg"), "Insert child item")
        self.addChildItemToolButton.triggered.connect(self.on_insert_child_item_action)      
        
        self.deleteItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-delete.svg"), "Delete item")  
        self.deleteItemToolButton.triggered.connect(self.on_delete_item)
        
        self.editItemToolButton = self.mainToolBar.addAction(QIcon("./mainToolbarIcons/Gnome-item-edit.svg"), "Edit item")
        self.editItemToolButton.triggered.connect(self.on_edit_item)
        
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
        # TODO: Hong - Is there any Python equivalent to __linux__ ?? If so, set self.directory = /home for Linux users
        self.filePath = ""
        self.directory = str(Path.home()) #Use pathlib to solve the problem
        self.dirtyBit = False # Indicates if tree has been modified

        return
        
    #--------------------------------------------------------------------------
    
    def on_insert_item_action(self):
        """Handler for 'add item' action"""

        self.itemTree.insert_task_item(True, False)
        self.dirtyBit = True
        print("adding an item")

        return
        
   #--------------------------------------------------------------------------
   
    def on_insert_child_item_action(self):
        """Handler for 'add child item' action"""

        self.itemTree.insert_task_item(True, True)
        self.dirtyBit = True
        print("add a child item")

        return
        
   #--------------------------------------------------------------------------

    def on_delete_item(self):
        """ Handler for "Delete" action """

        self.itemTree.delete_task_item()
        self.dirtyBit = True

        return

    #--------------------------------------------------------------------------

    def on_edit_item(self):
        """Handler for 'Open' menu item"""

        self.itemTree.edit_task_item()
        self.dirtyBit = True

        return

    #--------------------------------------------------------------------------

    def open_file(self, filePath):

        # Read XML file
        # TODO - Chung Tung Ching 
        if (__name__ =="__main__"):
            parser=xml.sax.make_parser()
            parser.setFeature(xml.sax.handler.feature_namespaces, 0)
            Handler =  xml_R.readHandler()
            parser.setContentHandler(Handler)
            parser.parse(filePath)
        # test
        #f = open(self.filePath) # Read the file
        #lines = f.read()
        #print(lines)
        #f.close()
        # test 

        self.dirtyBit = False     

        return

    #--------------------------------------------------------------------------    
    
    def on_open_action(self):
        """Handler for 'open' action"""
        # TODO - Hong
        # Get file path
        (self.filePath,filetype) = QFileDialog.getOpenFileName(self, "Open", self.directory, "Organiser file (*.xml);;Text Files (*.txt)")
        print("open file item") # Add txt for test

        if (self.filePath == ""):
            print("\nDeslect the choose")
            return

        # Use the pathlib package to deal with the different os file system
        # and get only the "dummy string.txt" part file name

        print("\nThe file you choosed is:")
        print(self.filePath)
        print("File type: ", filetype)
             
        # Separate self.filePath into self.directory + fileName strings: consider LUnix as well as Windows file paths
        # TODO - Hong
        fileName = Path(self.filePath).name
        self.directory = self.filePath[0:len(self.filePath)-len(fileName)]
        print("filename:")
        print(fileName)
        print("directory:")
        print(self.directory)

        #fileName = "dummy String"
        self.setWindowTitle("Organiser - " + fileName)
        
        self.open_file(self.filePath)
      
        return
        
    #--------------------------------------------------------------------------

    def save_file(self, filePath):

        # Write XML file
        # TODO 
        tree =ET.Element('Tree')
        parent = self.invisibleRootItem()
        target[0]=parent
        roll_whole_tree(parent)
        myfile = open(filePath, "w+")
        mynode =  correctform(tree)
        myfile.write( mynode )
        
        self.dirtyBit = False

        return

    #--------------------------------------------------------------------------

    def on_save_action(self):
   
        if (self.filePath == ""):
            # TODO - Hong : launch QFileDialog to prompt use for valid file name
            #self.filePath = ...
            (self.filePath, _) = QFileDialog.getOpenFileName(self, "Save", self.directory, "Organiser file (*.xml)")
            print("open file item") # test

            if (self.filePath == ""):
                print("\nDeslect the choose")
                return

            print("saving as", self.filePath)

        self.save_file(self.filePath)
        self.dirtyBit = False

        return

    #--------------------------------------------------------------------------

    def on_save_as_action(self):

        # Get file path to save to
        # TODO - Hong

        # self.save_file(newFilePath)
        # self.filepath = newFilePath
        
        (self.filePath, _) = QFileDialog.getOpenFileName(self, "Save as", self.directory, "Organiser file (*.xml)") #dialog directly
        print("open file item") # test

        if (self.filePath == ""):
            print("\nDeslect the choose")
            return

        print("saving as", self.filePath)

        self.save_file(self.filePath)
        self.dirtyBit = False

        return

    #--------------------------------------------------------------------------

    def on_about_action(self):
        # TODO - Hong
        aboutmessage = '''
Tutor: Peter Rockett

MainWindow: Hong Zhou

Interface to XML: Chung Tung Ching

SetPreferences: Yuqi Jin

Implement show_schedule() ＆ search_tree(): Tong Wang

ItemTree and TaskItem: Samuel Maher

NoteEditor and EditBox: Joseph-William Szetu

Spell_checker: Andrei Georgescu'''

        QMessageBox.about(self,"Developer List",aboutmessage)

        return

    #--------------------------------------------------------------------------
      
    def on_set_preferences_action(self):
        """Handler for 'Set preferences' menu action"""

        self.itemTree.set_item_tree_preferences()
        
        return
    
    #--------------------------------------------------------------------------   
    
    def on_quit_action(self):
        """Handler for 'quit' action"""
        # TODO - Hong
        # Check whether data needs to be auto-saved on exit
        if (self.dirtyBit):
            print("Prompt for saving file")
            # call message box?
            result = QMessageBox.information(self,"Quit","Do you want to save the file before exiting?",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            result = str(result)

            if "Yes" in result:
                print("Saved and Quit")
                self.on_save_action()
            else:
                self.close()
                print("The file didn't be saved!")
                return

        print("quitting application")
        self.close()
        
        return

#******************************************************************************

# Main program
if __name__ == "__main__":
    application = QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()

    # test
    #mainWindow.itemTree.add_task_item(0, "hello", "note1", 0, True, 0)
    #mainWindow.itemTree.add_task_item(0, "hello2", "note2", 0, True, 0)
    #mainWindow.itemTree.add_task_item(0, "first child", "note3", 0, True, 0)


    exit(application.exec_())   # Not sure why this still has to be `exec_` with a trailing underscore?

#******************************************************************************
