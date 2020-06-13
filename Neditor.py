from PySide2.QtWidgets import QToolBar, QTextEdit, QAction
from PySide2.QtGui import QFont, QTextDocument, QKeySequence, QIcon

import os

class NEdit():
    def __init__(self):
        self.toolbar = self.createToolbar()
        self.editBox = self.createEditBox()
        return
#---------------------------------------------------------------------------
    def displayNote(self, document):

        self.editBox.setDocument(document)
        return
#---------------------------------------------------------------------------
    def createToolbar(self):
        # Create main toolbar
        self.mainToolBar = QToolBar()
        self.mainToolBar.setMovable(False)

        #Buttons
        #Font Family
        #Font Size
        #Bold
        self.bold_button = QAction(QIcon(os.path.join('images', 'edit-bold.png')), "Bold")
        self.bold_button.setStatusTip("Bold")
        self.bold_button.setShortcut(QKeySequence.Bold)
        self.bold_button.setCheckable(True)
        self.bold_button.toggled.connect(lambda x: self.editBox.setFontWeight(QFont.Bold if x else QFont.Normal))
        self.mainToolBar.addAction(self.bold_button)
        #italic
        #underline  
        return(self.mainToolBar)
#---------------------------------------------------------------------------    
    def createEditBox(self):
        self.editBox = QTextEdit()

        return(self.editBox)
#---------------------------------------------------------------------------
    def action1(self):
        print("1")
