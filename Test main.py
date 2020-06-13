#! /usr/bin/env python3

#******************************************************************************
# Insert licence here!



#******************************************************************************

from sys import exit

from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide2.QtWidgets import QMenuBar, QMenu, QAction
from PySide2.QtWidgets import QToolBar
from PySide2.QtWidgets import QStatusBar

from ItemTree import *
from NoteEditor import NoteEditor
from Neditor import NEdit
#******************************************************************************

class MainWindow(QMainWindow):
    """
    Main application window
    :version:
    :author: pir
    """

   #--------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Organiser")
        self.mainLayout = QVBoxLayout()

        # Create menu bar & menus
        self.fileMenu = self.menuBar().addMenu("&File")
        self.openMenuAction = self.fileMenu.addAction("&Open")
        self.openMenuAction.triggered.connect(self.on_open_action)    # New-style connect!
        self.fileMenu.addSeparator()
        self.setPreferencesMenuAction = self.fileMenu.addAction("Set Preferences")
        self.setPreferencesMenuAction.triggered.connect(self.on_set_preferences_action)        
        self.fileMenu.addSeparator()
        self.quitMenuAction = self.fileMenu.addAction("&Quit")
        self.quitMenuAction.triggered.connect(self.on_quit_action)

        self.nEdit = NEdit()
        self.mainLayout.addWidget(self.nEdit.editBox)
        self.mainLayout.addWidget(self.nEdit.toolbar)

        # Set layout as the central widget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

        # TEST ONLY
        self.uniqueCounter = 0
        
        return
        
   #--------------------------------------------------------------------------
    
    def on_open_action(self):
        """Handler for 'open' action"""
        
        print("open file item")
        
        return
        
    #--------------------------------------------------------------------------
   
    def on_set_preferences_action(self):
        """Handler for 'set preferences' action"""

        self.itemTree.set_item_tree_preferences()
        
        return
    
    #--------------------------------------------------------------------------   
    
    def on_quit_action(self):
        """Handler for 'quit' action"""
        
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
    #mainWindow.itemTree.add_task_item(0, "hello", "note", 0, True, 0)
    #mainWindow.itemTree.add_task_item(0, "hello2", "note", 0, True, 0)
    #mainWindow.itemTree.add_task_item(0, "first child", "note", 0, True, 1)


    exit(application.exec_())   # Not sure why this still has to be `exec_` with a trailing underscore?

#******************************************************************************















