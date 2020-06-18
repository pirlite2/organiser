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
import enchant
from PySide2.QtWidgets import *
import time
#******************************************************************************


def EditBox(): #edit box prototpye
        return 'roboti'
#******************************************************************************
d = enchant.Dict("en_GB") # selecting UK English dictionary
def Spellcheck(word):
    suggest = d.suggest(word) #suggesting corrections
    listsize = len(suggest) #finding suggestion list size
    print("List size is %i" % listsize) #printing suggestion list size
    return suggest

word = EditBox()
suggest = Spellcheck(word)

class SpellCheckWindow(QWidget):        
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Spellchecking Error") #setting title
        self.setGeometry(300,300, 500,400) #setting window parameters
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)

        self.text = QLabel("%s seems to be spelled inccorectly, please choose an option:" % word) #text
        self.suggestion1 = QPushButton("%s" % suggest[0]) #adding text to buttons
        self.suggestion2 = QPushButton("%s" % suggest[1]) 
        self.suggestion3 = QPushButton("%s" % suggest[2]) 
        self.suggestion4 = QPushButton("Ignore")
        self.suggestion5 = QPushButton("Add word to dictionary")

        self.layout =  QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.suggestion1) #adding buttons to window
        self.layout.addWidget(self.suggestion2)
        self.layout.addWidget(self.suggestion3)
        self.layout.addWidget(self.suggestion4)
        self.layout.addWidget(self.suggestion5)

        self.suggestion1.clicked.connect(self.swap_word1) #adding functionality to buttons
        self.suggestion2.clicked.connect(self.swap_word2)
        self.suggestion3.clicked.connect(self.swap_word3)
        self.suggestion4.clicked.connect(self.ignore)
        self.suggestion5.clicked.connect(self.addword)

    def swap_word1(self): #swaping functionality
        word = suggest[0]
        print("Word is now %s" % word) #print the swap result
        sys.exit(0)
    def swap_word2(self): 
        word = suggest[1] #swaping functionality
        print("Word is now %s" % word)
        sys.exit(0)
    def swap_word3(self): #swaping functionality
        word = suggest[2]
        print("Word is now %s" % word)
        sys.exit(0)
    def ignore(self): #ignoring the spellcheker suggestion
        d.remove(word)
        print("Word is ignored") #print the ignore result
        sys.exit(0) 
    def addword(self): #adding word to user dictionary
        d.add(word)
        print("Word added to dictionary") #print the add to dictionary result
        sys.exit(0)

if d.check(word) is False: #if word is incorrect run spellcheker application
    print(d.suggest(word)) #print suggestion list
    myApp = QApplication(sys.argv) #running spellcheker loop
    window = SpellCheckWindow()
    window.show() #showing the window
    time.sleep(3) #resize the window to parameters after 3 seconds
    window.resize(600,400)
    myApp.exec_()

#******************************************************************************