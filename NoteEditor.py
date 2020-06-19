from PySide2.QtWidgets import QToolBar, QTextEdit, QAction, QFontComboBox, QComboBox, QWidget, QVBoxLayout
from PySide2.QtGui import QFont, QTextDocument, QKeySequence, QIcon

import os

font_sizes = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72, 84, 96, 110, 130]
DEFAULT_FONT_SIZE = 12.0


class NoteEditor (QWidget):
    """
    Container for NoteEditor instances 
    :version: 1.0
    :author: js
    """
    def __init__(self):
        super().__init__()

        #initialise the widgets needed
        self.mainLayout = QVBoxLayout()
        self.editBox = self.createEditBox()
        self.toolbar = self.createToolbar()

        #initial text settings 
        self.fontsize.setCurrentIndex(font_sizes.index(DEFAULT_FONT_SIZE))

        #set up layout
        self.mainLayout.addWidget(self.editBox)
        self.mainLayout.addWidget(self.toolbar)
        self.setLayout(self.mainLayout)
        return
#---------------------------------------------------------------------------
    def setDocument(self, document):
        self.editBox.setDocument(document)
        return
#---------------------------------------------------------------------------
    def createToolbar(self):
        # Create main toolbar
        self.mainToolBar = QToolBar()
        self.mainToolBar.setMovable(False)

        #Buttons
        #Font Family
        self.fonts_combo = QFontComboBox()
        self.fonts_combo.currentFontChanged.connect(self.fontChanged)
        self.mainToolBar.addWidget(self.fonts_combo)

        #Font Size
        self.fontsize = QComboBox()
        self.fontsize.addItems([str(s) for s in font_sizes])

        self.mainToolBar.addWidget(self.fontsize)
        self.fontsize.currentIndexChanged[str].connect(self.fontSizeChanged)
        self.mainToolBar.addSeparator()

        #Bold
        self.bold_button = QAction(QIcon(os.path.join('icons', 'bold.svg')), "Bold")
        self.bold_button.setStatusTip("Bold")
        self.bold_button.setCheckable(True)
        self.bold_button.toggled.connect(lambda x: self.editBox.setFontWeight(QFont.Bold if x else QFont.Normal))
        self.mainToolBar.addAction(self.bold_button)

        #italic
        self.italic_button = QAction(QIcon(os.path.join('icons', 'italic.svg')), "Italic")
        self.italic_button.setStatusTip("Italic")
        self.italic_button.setCheckable(True)
        self.italic_button.toggled.connect(self.editBox.setFontItalic)
        self.mainToolBar.addAction(self.italic_button)

        #underline
        self.underline_button = QAction(QIcon(os.path.join('icons', 'underline.svg')), "Underline")
        self.underline_button.setStatusTip("Underline")
        self.underline_button.setCheckable(True)
        self.underline_button.toggled.connect(self.editBox.setFontUnderline)
        self.mainToolBar.addAction(self.underline_button)

        #alignment

        return(self.mainToolBar)
#---------------------------------------------------------------------------    
    def createEditBox(self):
        editBox = QTextEdit()
        editBox.setFontPointSize(DEFAULT_FONT_SIZE)


        return(editBox)
#---------------------------------------------------------------------------
    def fontChanged(self):
        font = self.fonts_combo.currentFont()
        self.editBox.setCurrentFont(font)
        self.fontSizeChanged()
        return
#---------------------------------------------------------------------------
    def fontSizeChanged(self):

        font_size = self.fontsize.currentText()
        self.editBox.setFontPointSize(float(font_size))
        self.fontsize.setCurrentText(font_size)

        return
