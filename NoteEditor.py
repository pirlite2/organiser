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

import os
import json

from PySide2.QtCore import Qt, QSize

from PySide2.QtGui import QTextDocument, QTextCursor, QTextCharFormat, QColor
from PySide2.QtGui import QFont, QKeySequence, QIcon

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide2.QtWidgets import QComboBox, QFontComboBox, QToolBar, QTextEdit, QAction

#******************************************************************************

fontSizePickers = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72, 84, 96]
defaultfontSize = 11.0

#******************************************************************************

class NoteEditor(QWidget):
    """
    :version:
    :author: pir, Joseph-William Szetu
    """

    #--------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        #self.setWindowFlag(0x00000012, True)

        widgetLayout = QVBoxLayout()

        self.noteEditBox = QTextEdit()
        self.noteEditBox.setFontPointSize(defaultfontSize)
        self.noteEditBox.setFont(QFont('Helvtica', defaultfontSize))
        self.noteEditBox.textChanged.connect(self.textHasChanged)

        editToolbar = QToolBar()
        editToolbar.setMovable(False)
        editToolbar.setIconSize(QSize(18, 18))

        # Buttons
        # Font Colour Picker
        self.fontColourPicker = QComboBox()
        with open(os.path.join('colours', 'colours.json')) as f:
            self.colours = json.load(f)
        self.fontColourPicker.addItems(self.colours.keys())
        #self.fontColourPicker.setStatusTip("Text Colour")
        self.fontColourPicker.setToolTip("Select font colour")
        editToolbar.addWidget(self.fontColourPicker)
        self.fontColourPicker.setCurrentIndex(0)
        self.fontColourPicker.currentIndexChanged.connect(self.colourPickerChanged)

        # Text Highlight Colour Picker
        self.textHighlight = QComboBox()
        self.textHighlight.addItems(self.colours.keys())
        self.textHighlight.setCurrentIndex(1)
        #self.textHighlight.setStatusTip("Highlight Colour")
        self.textHighlight.setToolTip("Highlight Colour")
        editToolbar.addWidget(self.textHighlight)
        self.textHighlight.currentIndexChanged.connect(self.textHighlightChanged)

        # Font Family
        self.fontFamilyPicker = QFontComboBox()
        self.fontFamilyPicker.setStatusTip("Font")
        self.fontFamilyPicker.currentFontChanged.connect(self.fontChanged)
        editToolbar.addWidget(self.fontFamilyPicker)

        # Font Size
        self.fontSizePicker = QComboBox()
        self.fontSizePicker.addItems([str(s) for s in fontSizePickers])
        self.fontSizePicker.setCurrentIndex(fontSizePickers.index(defaultfontSize))
        self.fontSizePicker.setStatusTip("Font Size")
        editToolbar.addWidget(self.fontSizePicker)
        self.fontSizePicker.currentIndexChanged.connect(self.fontSizePickerChanged)
        editToolbar.addSeparator()

        # Bold
        self.boldButton = QAction(QIcon("./editToolbarIcons/Gnome-format-text-bold.svg"), "Bold")
        #self.boldButton.setStatusTip("Bold")
        self.boldButton.setCheckable(True)
        self.boldButton.setToolTip("Bold")
        self.boldButton.toggled.connect(lambda x: self.noteEditBox.setFontWeight(QFont.Bold if x else QFont.Normal))
        editToolbar.addAction(self.boldButton)

        # Italic
        self.italicButton = QAction(QIcon("./editToolbarIcons/Gnome-format-text-italic.svg"), "Italic")
        #self.italicButton = QAction(QIcon(os.path.join('icons', 'italic.svg')), "Italic")
        self.italicButton.setStatusTip("Italic")
        self.italicButton.setCheckable(True)
        self.italicButton.setToolTip("Italic")
        self.italicButton.toggled.connect(self.noteEditBox.setFontItalic)
        editToolbar.addAction(self.italicButton)

        # Underline
        self.underlineButton = QAction(QIcon("./editToolbarIcons/Gnome-format-text-underline.svg"), "Underline")
        self.underlineButton.setStatusTip("Underline")
        self.underlineButton.setCheckable(True)
        self.underlineButton.setToolTip("Underline")
        self.underlineButton.toggled.connect(self.noteEditBox.setFontUnderline)
        editToolbar.addAction(self.underlineButton)

        widgetLayout.addWidget(editToolbar)     
       
        widgetLayout.addWidget(self.noteEditBox)
        self.setLayout(widgetLayout)
              
        return

    #--------------------------------------------------------------------------

    def setNoteDocument(self, document):
        """
        Set document of the text editor
        :version:
        :author: pir
        """

        self.noteEditBox.setDocument(document)

        return

    #---------------------------------------------------------------------------
    
    def textHasChanged(self):
        """
        Interface to spellchecker???
        :version:
        :author: js
        """

        plainText = self.noteEditBox.toPlainText()

        if(plainText[-1] == ' ' or plainText[-1] == '\n'):
            print("Text changed...>>> " + self.noteEditBox.toPlainText())
            """ INSERT HERE CALL TO SPELL CHECK MODULE I.E
                self.editBox.spell_check(plainText)
            """
        return

    #---------------------------------------------------------------------------

    def fontChanged(self):
        """

        :version:
        :author: js
        """

        font = self.fontFamilyPicker.currentFont()
        self.noteEditBox.setCurrentFont(font)
        self.fontSizePickerChanged()
        print("font changed")
        return
    
    #---------------------------------------------------------------------------
    
    def fontSizePickerChanged(self):
        """

        :version:
        :author: js
        """

        fontSize = self.fontSizePicker.currentText()
        self.noteEditBox.setFontPointSize(float(fontSize))
        self.fontSizePicker.setCurrentText(fontSize)
        print("font size changed")

        return

    #---------------------------------------------------------------------------
    
    def colourPickerChanged(self):
        """

        :version:
        :author: js
        """

        currentColour = self.fontColourPicker.currentText()
        print("font colour changed")
        (r,g,b) = self.colours[currentColour]['rgb']
        self.noteEditBox.setTextColor(QColor(r,g,b))

        return

    #---------------------------------------------------------------------------
    
    def textHighlightChanged(self):
        """

        :version:
        :author: js
        """

        currentColour = self.textHighlight.currentText()
        print("text background colour changed")
        r,g,b = self.colours[currentColour]['rgb']
        self.noteEditBox.setTextBackgroundColor(QColor(r,g,b))

        return

    #--------------------------------------------------------------------------

    def spell_check(self, document):
        """
        Spell check document
        :version:
        :author: pir & ???
        """

        documentText = document.toPlainText()
        wordList = documentText.split()

        # test
        for i in range(0, len(wordList)):
            print(wordList[i])
        #test

        # find misspelled word & correct it
        wrongSpelling = "folls"
        correctSpelling = "falls"
        currentTextCursor = QTextCursor(document)
        textCursor = document.find(wrongSpelling, currentTextCursor, QTextDocument.FindCaseSensitively or QTextDocument.FindWholeWords)
        print("selected word = ", textCursor.selectedText())

        underlineFormat = QTextCharFormat()
        underlineFormat.setUnderlineColor(QColor(255, 0, 0))
        underlineFormat.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
        textCursor.setCharFormat(underlineFormat)

        noUnderlineFormat = QTextCharFormat()
        noUnderlineFormat.setUnderlineStyle(QTextCharFormat.NoUnderline)
        #textCursor.insertText(correctSpelling, noUnderlineFormat) # Uncomment to correct mispelled word & remove wiggly red underline

        # IMPLEMENTATION NOTES: 
        # try QTextEdit.cursorForPosition(pos) to get QTextCursor at mouse-right click position. does the cursor contain the underlined (mispelled) word?

        return

#******************************************************************************

if __name__ == "__main__":
    application = QApplication([])

    mainWindow = QMainWindow()
    noteEditor = NoteEditor()

    mainWindow.setCentralWidget(noteEditor)
    mainWindow.show()

    document = QTextDocument("the rain in Spaun folls maily on the plaine\n\n hello world")
    noteEditor.setNoteDocument(document)
    noteEditor.spell_check(document)

    exit(application.exec_()) 

#******************************************************************************

