from PySide2.QtWidgets import QToolBar, QTextEdit, QAction, QFontComboBox, QComboBox, QWidget, QVBoxLayout
from PySide2.QtGui import QFont, QTextDocument, QKeySequence, QIcon, QColor
from PySide2.QtCore import QSize

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
        self.document = document
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
        if(len(plainText) >= 1 ):
            if(plainText[-1] == ' '):
                """ INSERT HERE CALL TO SPELL CHECK MODULE I.E
                    self.editBox.spell_check(self.document)
                """

        return
#---------------------------------------------------------------------------
    def fontChanged(self):

        font = self.fontFamilyPicker.currentFont()
        self.editBox.setCurrentFont(font)
        self.fontSizePickerChanged()
        return
#---------------------------------------------------------------------------
    def fontSizePickerChanged(self):

        fontSize = self.fontSizePicker.currentText()
        self.editBox.setFontPointSize(float(fontSize))
        self.fontSizePicker.setCurrentText(fontSize)

    def setNoteDocument(self, document):
        """
        Set document of the text editor
        :version:
        :author: pir
        """

        self.noteEditBox.setDocument(document)

        return

    #--------------------------------------------------------------------------
    
    def spell_check(self, document):
        """
        Spell check document
        :version:
        :author: pir & Andrei
        """
        d = enchant.Dict("en_GB") #selecting the English UK dictionary
        self.document = document
        documentText = self.document.toPlainText() # converting to plain text
        wordList = documentText.split() # spliting the sentance into individual words
        self.wordDict = {} #creat dictionary for misspelled and suggestions

        for s in range(0,len(wordList)):
            if d.check(wordList[s]) is False: #if the word is misspeled find suggestions and highlight with a red underline
                
                wrongSpelling = wordList[s] # store the misspeled word
                correctSpelling = d.suggest(wordList[s]) # suggest correct spelling

                for t in range(0,len(correctSpelling)): #looping
                    self.list.addItem(correctSpelling[t]) #add correct spelling to the list
                    self.wordDict[correctSpelling[t]] = wordList[s] # match the correct spelling to the misspelled word

                    currentTextCursor = QTextCursor(self.document) #setting the cursor 
                    textCursor = self.document.find(wrongSpelling, currentTextCursor, QTextDocument.FindCaseSensitively or QTextDocument.FindWholeWords) #finding the misspelled word
        return
#---------------------------------------------------------------------------
    def colourPickerChanged(self):

        currentColour = self.fontColourPicker.currentText()
        r,g,b = self.colours[currentColour]['rgb']
        self.editBox.setTextColor(QColor(r,g,b))

                    underlineFormat = QTextCharFormat()
                    underlineFormat.setUnderlineColor(QColor(255, 0, 0)) #setting underline colour to red
                    underlineFormat.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline) #setting the underline style
                    textCursor.setCharFormat(underlineFormat) #applying settinggs to the cursor

                    noUnderlineFormat = QTextCharFormat()
                    noUnderlineFormat.setUnderlineStyle(QTextCharFormat.NoUnderline) # settings for removing the underline
                    #self.list.itemClicked(self.list_choice) #connection not working
                 
        return
#---------------------------------------------------------------------------
    def textHighlightChanged(self):

        currentColour = self.textHighlight.currentText()
        r,g,b = self.colours[currentColour]['rgb']
        self.editBox.setTextBackgroundColor(QColor(r,g,b))

    def list_choice(self):
        currentTextCursor = QTextCursor(self.document)
        noUnderlineFormat = QTextCharFormat()

        noUnderlineFormat.setUnderlineStyle(QTextCharFormat.NoUnderline)
        textCursor = self.document.find(words[0], currentTextCursor, QTextDocument.FindCaseSensitively or QTextDocument.FindWholeWords)
        textCursor.insertText(words[1], noUnderlineFormat) # Uncoment to correct mispelled word & remove wiggly red underline
        self.spell_check(self.document) #run the program again to remove replaced words
        

#******************************************************************************

if __name__ == "__main__":
    application = QApplication([])

    mainWindow = QMainWindow()
    noteEditor = NoteEditor()
  
    mainWindow.setCentralWidget(noteEditor)
    mainWindow.show() # showing the window

    document = QTextDocument("I alerady fuond the solution btu it’s good to hvae more than") #prototype input text for spellchecker
    noteEditor.setNoteDocument(document)
    noteEditor.spell_check(document) #inputing to spellchecker

    exit(application.exec_()) #clean app exit

#******************************************************************************

# Old code... some might be salvaged and reused?


# d = enchant.Dict("en_GB")
# suggest = EditBox.Spellcheck(word) ##suggesting corrections
# if d.check(word) is False: #if word is incorrect run spellcheker application
#     print(d.suggest(word)) #print suggestion list
#     myApp1 = QApplication(sys.argv) #running spellcheker loop
#     window = EdiBox.SpellCheckWindow()
#     window.show() #showing the window
#     time.sleep(3) #resize the window to parameters after 3 seconds
#     window.resize(600,400)
#     myApp1.exec_()


# d = enchant.Dict("en_GB") # selecting UK English dictionary
# def Spellcheck(word):
#     suggest = d.suggest(word) #suggesting corrections
#     listsize = len(suggest) #finding suggestion list size
#     print("List size is %i" % listsize) #printing suggestion list size
#     return suggest

# word = EditBox()
# suggest = Spellcheck(word)

# class SpellCheckWindow(QWidget):        
#     def __init__(self):
#         QWidget.__init__(self)
#         self.setWindowTitle("Spellchecking Error") #setting title
#         self.setGeometry(300,300, 500,400) #setting window parameters
#         self.setMinimumHeight(100)
#         self.setMinimumWidth(250)
#         self.setMaximumHeight(200)
#         self.setMaximumWidth(800)

#         self.text = QLabel("%s seems to be spelled inccorectly, please choose an option:" % word) #text
#         self.suggestion1 = QPushButton("%s" % suggest[0]) #adding text to buttons
#         self.suggestion2 = QPushButton("%s" % suggest[1]) 
#         self.suggestion3 = QPushButton("%s" % suggest[2]) 
#         self.suggestion4 = QPushButton("Ignore")
#         self.suggestion5 = QPushButton("Add word to dictionary")

#         self.layout =  QVBoxLayout()
#         self.setLayout(self.layout)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.suggestion1) #adding buttons to window
#         self.layout.addWidget(self.suggestion2)
#         self.layout.addWidget(self.suggestion3)
#         self.layout.addWidget(self.suggestion4)
#         self.layout.addWidget(self.suggestion5)

#         self.suggestion1.clicked.connect(self.swap_word1) #adding functionality to buttons
#         self.suggestion2.clicked.connect(self.swap_word2)
#         self.suggestion3.clicked.connect(self.swap_word3)
#         self.suggestion4.clicked.connect(self.ignore)
#         self.suggestion5.clicked.connect(self.addword)

#     def swap_word1(self): #swaping functionality
#         word = suggest[0]
#         print("Word is now %s" % word) #print the swap result
#         sys.exit(0)
#     def swap_word2(self): 
#         word = suggest[1] #swaping functionality
#         print("Word is now %s" % word)
#         sys.exit(0)
#     def swap_word3(self): #swaping functionality
#         word = suggest[2]
#         print("Word is now %s" % word)
#         sys.exit(0)
#     def ignore(self): #ignoring the spellcheker suggestion
#         d.remove(word)
#         print("Word is ignored") #print the ignore result
#         sys.exit(0) 
#     def addword(self): #adding word to user dictionary
#         d.add(word)
#         print("Word added to dictionary") #print the add to dictionary result
#         sys.exit(0)

# if d.check(word) is False: #if word is incorrect run spellcheker application
#     print(d.suggest(word)) #print suggestion list
#     myApp = QApplication(sys.argv) #running spellcheker loop
#     window = SpellCheckWindow()
#     window.show() #showing the window
#     time.sleep(3) #resize the window to parameters after 3 seconds
#     window.resize(600,400)
#     myApp.exec_()
