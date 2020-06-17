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
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QWidget, QLabel)
import time
#******************************************************************************
word = 'pinaple'

class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("Spellchecking Error")
        self.setGeometry(300,300, 500,400)
        self.setMinimumHeight(100)
        self.setMinimumWidth(250)
        self.setMaximumHeight(200)
        self.setMaximumWidth(800)
        self.label1 = QLabel("Word is spelled incorrectly")
        self.label1.show()

myApp = QApplication(sys.argv)
window = Window()
window.show()
 
time.sleep(3)
window.resize(600,400)
#window.repaint()
 
myApp.exec_()
sys.exit(0)   
    # def spell_check(word):

    #    d = enchant.Dict("en_US")
       
     #   if d.check(word) is False:
           # d.suggest(word)

#******************************************************************************