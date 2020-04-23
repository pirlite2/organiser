#! /usr/bin/env python3

#******************************************************************************
# Example Qt main program -- pir -- 17.4.2020


#******************************************************************************

from sys import exit
#from PySide2 import QtCore
#from PySide2 import QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QSplitter
from PySide2.QtWidgets import QMenuBar, QToolBar, QStatusBar
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem
from PySide2.QtWidgets import QTextEdit

#******************************************************************************
# Insert licence here!

#******************************************************************************

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Organiser")
        self.mainLayout = QVBoxLayout()

        # Create menu bar & menus
        #TODO

        # Create main toolbar
        self.mainToolBar = QToolBar(self)
        self.mainToolBar.setMovable(False)
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
    
    # def on_signal_handler(self):
    #     self.text.setText(random.choice(self.hello))

#******************************************************************************

# Main program
if __name__ == "__main__":
    application = QApplication([])

    mainWindow = MainWindow()
    mainWindow.show()

    exit(application.exec_())   # Not sure why this has to be `exec_` with a trailing underscore?

#******************************************************************************