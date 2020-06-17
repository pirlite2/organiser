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
word = 'roboti'

class SpellCheckWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Spellchecking Error")
        self.setGeometry(300,300, 500,400)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)

        self.text = QLabel("%s seems to be spelled inccorectly, please choose an option" % word)
        self.suggestion1 = QPushButton("%s" % suggest[0])
        self.suggestion2 = QPushButton("%s" % suggest[1])
        self.suggestion3 = QPushButton("%s" % suggest[2])

        self.layout =  QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.suggestion1)
        self.layout.addWidget(self.suggestion2)
        self.layout.addWidget(self.suggestion3)
        
        self.suggestion1.clicked.connect(self.swap_word1)
        self.suggestion2.clicked.connect(self.swap_word2)
        self.suggestion3.clicked.connect(self.swap_word3)



    def swap_word1(self):
        word = suggest[0]
       
    def swap_word2(self):
        word = suggest[1]
        
    def swap_word3(self):
        word = suggest[2]
        
d = enchant.Dict("en_GB")
suggest = d.suggest(word)
listsize = len(suggest)
print("List size is %i" % listsize)
if d.check(word) is False:
    print(d.suggest(word))
    myApp = QApplication(sys.argv)
    window = SpellCheckWindow()
    window.show()
    time.sleep(3)
    window.resize(600,400)
    myApp.exec_()
    sys.exit(0)   

#******************************************************************************