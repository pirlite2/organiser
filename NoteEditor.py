from PySide2.QtWidgets import QToolBar, QTextEdit, QAction, QFontComboBox, QComboBox, QWidget, QVBoxLayout
from PySide2.QtGui import QFont, QTextDocument, QKeySequence, QIcon, QColor
from PySide2.QtCore import QSize
from EditBox import EditBox

import os
import json

fontSizePickers = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72, 84, 96, 110, 130]
defaultfontSize = 18.0


class NoteEditor (QWidget):
    """
    Container for NoteEditor instances 
    :version: 1.0
    :author: js
    """
    def __init__(self):
        super().__init__()

        #initialise the widgets needed
        self.layout = QVBoxLayout()
        self.editBox = self.createEditBox()
        self.toolbar = self.createToolbar()

        #initial text settings 
        

        #set up layout
        self.layout.addWidget(self.editBox)
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)
        return
#---------------------------------------------------------------------------
    def setDocument(self, document):
        self.editBox.setDocument(document)
        return
#---------------------------------------------------------------------------
    def createToolbar(self):
        # Create main toolbar
        mainToolBar = QToolBar()
        mainToolBar.setMovable(False)

        mainToolBar.setIconSize(QSize(18, 18))

        #Buttons
        #Font Colour Picker
        self.fontColourPicker = QComboBox()
        with open(os.path.join('colours', 'colours.json')) as f:
            self.colours = json.load(f)
        self.fontColourPicker.addItems(self.colours.keys())
        self.fontColourPicker.setStatusTip("Text Colour")
        mainToolBar.addWidget(self.fontColourPicker)
        self.fontColourPicker.setCurrentIndex(0)
        self.fontColourPicker.currentIndexChanged.connect(self.colourPickerChanged)

        #Text Highlight Colour Picker
        self.textHighlight = QComboBox()
        self.textHighlight.addItems(self.colours.keys())
        self.textHighlight.setCurrentIndex(1)
        self.textHighlight.setStatusTip("Highlight Colour")
        mainToolBar.addWidget(self.textHighlight)
        self.textHighlight.currentIndexChanged.connect(self.textHighlightChanged)

        #Font Family
        self.fontFamilyPicker = QFontComboBox()
        self.fontFamilyPicker.setStatusTip("Font")
        self.fontFamilyPicker.currentFontChanged.connect(self.fontChanged)
        mainToolBar.addWidget(self.fontFamilyPicker)

        #Font Size
        self.fontSizePicker = QComboBox()
        self.fontSizePicker.addItems([str(s) for s in fontSizePickers])
        self.fontSizePicker.setCurrentIndex(fontSizePickers.index(defaultfontSize))
        self.fontSizePicker.setStatusTip("Font Size")
        mainToolBar.addWidget(self.fontSizePicker)
        self.fontSizePicker.currentIndexChanged.connect(self.fontSizePickerChanged)
        mainToolBar.addSeparator()

        #Bold
        self.boldButton = QAction(QIcon(os.path.join('icons', 'bold.svg')), "Bold")
        self.boldButton.setStatusTip("Bold")
        self.boldButton.setCheckable(True)
        self.boldButton.toggled.connect(lambda x: self.editBox.setFontWeight(QFont.Bold if x else QFont.Normal))
        mainToolBar.addAction(self.boldButton)

        #Italic
        self.italicButton = QAction(QIcon(os.path.join('icons', 'italic.svg')), "Italic")
        self.italicButton.setStatusTip("Italic")
        self.italicButton.setCheckable(True)
        self.italicButton.toggled.connect(self.editBox.setFontItalic)
        mainToolBar.addAction(self.italicButton)

        #Underline
        self.underlineButton = QAction(QIcon(os.path.join('icons', 'underline.svg')), "Underline")
        self.underlineButton.setStatusTip("Underline")
        self.underlineButton.setCheckable(True)
        self.underlineButton.toggled.connect(self.editBox.setFontUnderline)
        mainToolBar.addAction(self.underlineButton)

        #alignment

        return(mainToolBar)
#---------------------------------------------------------------------------    
    def createEditBox(self):

        editBox = QTextEdit()
        editBox.setFontPointSize(defaultfontSize)
        editBox.setFont(QFont('Times', defaultfontSize))
        editBox.setPlaceholderText("New Note.....")
        editBox.textChanged.connect(self.textHasChanged)

        return(editBox)
#---------------------------------------------------------------------------
    def textHasChanged(self):
        plainText = self.editBox.toPlainText()

        if(plainText[-1] == ' '):
            print("Text changed...>>> " + self.editBox.toPlainText())
            """ INSERT HERE CALL TO SPELL CHECK MODULE I.E
                self.editBox.spell_check(plainText)
            """
        return
#---------------------------------------------------------------------------
    def fontChanged(self):

        font = self.fontFamilyPicker.currentFont()
        self.editBox.setCurrentFont(font)
        self.fontSizePickerChanged()
        print("font changed")
        return
#---------------------------------------------------------------------------
    def fontSizePickerChanged(self):

        fontSize = self.fontSizePicker.currentText()
        self.editBox.setFontPointSize(float(fontSize))
        self.fontSizePicker.setCurrentText(fontSize)
        print("font size changed")

        return
#---------------------------------------------------------------------------
    def colourPickerChanged(self):

        currentColour = self.fontColourPicker.currentText()
        print("font colour changed")
        r,g,b = self.colours[currentColour]['rgb']
        self.editBox.setTextColor(QColor(r,g,b))

        return
#---------------------------------------------------------------------------
    def textHighlightChanged(self):

        currentColour = self.textHighlight.currentText()
        print("text background colour changed")
        r,g,b = self.colours[currentColour]['rgb']
        self.editBox.setTextBackgroundColor(QColor(r,g,b))

        return