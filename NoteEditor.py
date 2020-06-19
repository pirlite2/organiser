from PySide2.QtWidgets import QToolBar, QTextEdit, QAction, QFontComboBox, QComboBox, QWidget, QVBoxLayout, QListWidget, QSplitter
from PySide2.QtGui import QFont, QTextDocument, QKeySequence, QIcon, QColor ,QTextCharFormat, QTextCursor
from PySide2.QtCore import QSize

import os
import json
import enchant

fontSizePickers = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72, 84, 96, 110, 130]
defaultfontSize = 18.0


class NoteEditor (QWidget):
    """
    Container for NoteEditor instances 
    :version: 1.0
    :author: Jowi, Andrei, pir
    """
    def __init__(self):
        super().__init__()
        """
            Container for NoteEditor instances 
            :version: 1.0
            :author: Jowi, Andrei, pir
            """
        #config Layouts
        self.mainLayout = QVBoxLayout()
        self.subLayout = QVBoxLayout()
        self.editorWidget = QWidget()

        self.splitter = QSplitter()
        self.splitter.setHandleWidth(2)

        self.editBox = self.createEditBox()
        self.toolbar = self.createToolbar()
        self.document = QTextDocument()
        self.list = QListWidget()

        #set up layouts
        self.subLayout.addWidget(self.editBox)
        self.subLayout.addWidget(self.toolbar)
        self.editorWidget.setLayout(self.subLayout)

        self.splitter.addWidget(self.editorWidget)      
        self.splitter.addWidget(self.list)

        self.mainLayout.addWidget(self.splitter)
        self.setLayout(self.mainLayout)
        return
#---------------------------------------------------------------------------
    def setNoteDocument(self, document):
        """
        Sets the QTextDocument into the editor
        :version: 1.0
        :author: Jowi
        """
        self.editBox.setDocument(document)
        self.document = document
        return
#---------------------------------------------------------------------------
    def createToolbar(self):
        """
        Creates the formatting toolbar
        :version: 1.0
        :author: Jowi
        """
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
        """
        Creates the editbox where the user types 
        :version: 1.0
        :author: Jowi
        """
        editBox = QTextEdit()
        editBox.setFontPointSize(defaultfontSize)
        editBox.setFont(QFont('Times', defaultfontSize))
        editBox.setPlaceholderText("New Note.....")
        editBox.textChanged.connect(self.textHasChanged)

        return(editBox)
#---------------------------------------------------------------------------
    def textHasChanged(self):
        """
        handler for the spell checker signals at every 
        change in editBox
        :version: 1.0
        :author: Jowi
        """
        plainText = self.editBox.toPlainText()
        if(len(plainText) >= 1 ):
            if(plainText[-1] == ' '):
                self.spell_check()
        return
#---------------------------------------------------------------------------
    def fontChanged(self):
        """
        handler for changing the font family
        :version: 1.0
        :author: Jowi
        """
        font = self.fontFamilyPicker.currentFont()
        self.editBox.setCurrentFont(font)
        self.fontSizePickerChanged()
        return
#---------------------------------------------------------------------------
    def fontSizePickerChanged(self):
        """
        handler for changing the font size
        :version: 1.0
        :author: Jowi
        """
        fontSize = self.fontSizePicker.currentText()
        self.editBox.setFontPointSize(float(fontSize))
        self.fontSizePicker.setCurrentText(fontSize)
#---------------------------------------------------------------------------
    def colourPickerChanged(self):
        """
        handler for changing the font colour
        :version: 1.0
        :author: Jowi
        """
        currentColour = self.fontColourPicker.currentText()
        r,g,b = self.colours[currentColour]['rgb']
        self.editBox.setTextColor(QColor(r,g,b))
        return
#---------------------------------------------------------------------------
    def textHighlightChanged(self):
        """
        handler for changing the highlight colour
        :version: 1.0
        :author: Jowi
        """
        currentColour = self.textHighlight.currentText()
        r,g,b = self.colours[currentColour]['rgb']
        self.editBox.setTextBackgroundColor(QColor(r,g,b))
        return
#---------------------------------------------------------------------------
    def list_choice(self):
        """
        list selection connect
        :version:
        :author: pir & Andrei
        """
        currentTextCursor = QTextCursor(self.document)
        noUnderlineFormat = QTextCharFormat()

        noUnderlineFormat.setUnderlineStyle(QTextCharFormat.NoUnderline)
        textCursor = self.document.find(words[0], currentTextCursor, QTextDocument.FindCaseSensitively or QTextDocument.FindWholeWords)
        textCursor.insertText(words[1], noUnderlineFormat) # Uncomment to correct misspelled word & remove wiggly red underline
        self.spell_check() #run the program again to remove replaced words
        return
#--------------------------------------------------------------------------
    def spell_check(self):
        """
        Spell check document
        :version:
        :author: pir & Andrei
        """
        self.editBox.blockSignals(True) #Blocks signal to avoid infinite loop 
        self.list.clear()
        d = enchant.Dict("en_GB") #selecting the English UK dictionary
        #self.document = document
        documentText = self.document.toPlainText() # converting to plain text
        wordList = documentText.split() # spliting the sentence into individual words
        self.wordDict = {} #create dictionary for misspelled and suggestions

        for s in range(0,len(wordList)):
            if d.check(wordList[s]) is False: #if the word is misspelled find suggestions and highlight with a red underline
                
                wrongSpelling = wordList[s] # store the misspelled word
                correctSpelling = d.suggest(wordList[s]) # suggest correct spelling

                for t in range(0,len(correctSpelling)): #looping
                    self.list.addItem(correctSpelling[t]) #add correct spelling to the list
                    self.wordDict[correctSpelling[t]] = wordList[s] # match the correct spelling to the misspelled word

                    currentTextCursor = QTextCursor(self.document) #setting the cursor 
                    textCursor = self.document.find(wrongSpelling, currentTextCursor, QTextDocument.FindCaseSensitively or QTextDocument.FindWholeWords) #finding the misspelled word

                    
                    underlineFormat = QTextCharFormat()
                    underlineFormat = textCursor.charFormat() #loads current formatting
                    underlineFormat.setUnderlineColor(QColor(255, 0, 0)) #setting underline colour to red
                    underlineFormat.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline) #setting the underline style

                    textCursor.setCharFormat(underlineFormat) #applying settings to the cursor

                    noUnderlineFormat = QTextCharFormat()
                    noUnderlineFormat.setUnderlineStyle(QTextCharFormat.NoUnderline) # settings for removing the underline
                    #self.list.itemClicked(self.list_choice) #connection not working
                self.list.addItem("------------------") #Added seperator 
        self.editBox.blockSignals(False) #Re-enable signals
        return