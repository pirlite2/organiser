#! /usr/bin/env python3

# Example Qt main program -- pir -- 17.4.2020

#******************************************************************************
# Insert licence here!



#******************************************************************************

from sys import exit
#from PySide2.QtCore import ???
#from PySide2.QtGui import ???
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide2.QtWidgets import QMenuBar, QMenu, QAction
from PySide2.QtWidgets import QToolBar
from PySide2.QtWidgets import QStatusBar
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem
from PySide2.QtWidgets import QTextEdit

from exampleDialog import ExampleDialog

#******************************************************************************

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Organiser")
        self.mainLayout = QVBoxLayout()

        # Create menu bar & menus
        self.fileMenu = self.menuBar().addMenu("&File")
        self.openMenuAction = self.fileMenu.addAction("&Open")
        self.openMenuAction.triggered.connect(self.on_open_action)    # New-style connect!
        self.fileMenu.addSeparator()
        self.quitMenuAction = self.fileMenu.addAction("&Quit")
        self.quitMenuAction.triggered.connect(self.on_quit_action)
        
        # Create main toolbar
        self.mainToolBar = QToolBar()
        self.mainToolBar.setMovable(False)
        self.openToolButton = self.mainToolBar.addAction("open")    # Replace with suitable icon      
        self.openToolButton.triggered.connect(self.on_open_action)
        self.addToolBar(self.mainToolBar)
        self.mainLayout.addWidget(self.mainToolBar)

        # Configure window splitter
        self.splitter = QSplitter()
        self.splitter.setHandleWidth(2)

        # Configure tree widget
        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderHidden(True)
        self.splitter.addWidget(self.treeWidget)
        
        # Configure text edit class
        self.editBox = QTextEdit()  # sub-class this?
        self.splitter.addWidget(self.editBox)
        self.mainLayout.addWidget(self.splitter)

        # Is a status bar needed in this application?
        self.statusBar = QStatusBar()
        self.mainLayout.addWidget(self.statusBar)

        # Set layout as the central widget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.mainWidget)

    #--------------------------------------------------------------------------
    
    def on_open_action(self):
        """Handler for 'open' action"""
        print("open a file")
        exampleDialog = ExampleDialog("Example dialog")
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

    exit(application.exec_())   # Not sure why this still has to be `exec_` with a trailing underscore?

#******************************************************************************
