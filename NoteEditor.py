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

from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import *
import EditBox
import enchant
import sys
import time



#******************************************************************************
word = ''
class NoteEditor(QWidget):
    """
    :version:
    :author:
    """

    #--------------------------------------------------------------------------


    #--------------------------------------------------------------------------

    def __init__(self):
        super().__init__()

        widgetLayout = QVBoxLayout()
        self.editToolbar = QToolBar()
        widgetLayout.addWidget(self.editToolbar)
        self.noteEditBox = QTextEdit()
        widgetLayout.addWidget(self.noteEditBox)
        self.setLayout(widgetLayout)
              
        return

    #--------------------------------------------------------------------------

    def setNoteDocument(self, document):
        """
        Set document of the text editor
        :version:
        :author:
        """

        self.noteEditBox.setDocument(document)

        return
word = 'reckl'
#******************************************************************************
d = enchant.Dict("en_GB")
suggest = EditBox.Spellcheck(word) ##suggesting corrections
if d.check(word) is False: #if word is incorrect run spellcheker application
    print(d.suggest(word)) #print suggestion list
    myApp1 = QApplication(sys.argv) #running spellcheker loop
    window = EdiBox.SpellCheckWindow()
    window.show() #showing the window
    time.sleep(3) #resize the window to parameters after 3 seconds
    window.resize(600,400)
    myApp1.exec_()