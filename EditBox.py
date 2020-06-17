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
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QTextEdit


#******************************************************************************
class Spellcheck_alert(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("Spellchecking error")

class EditBox (QTextEdit):

    """
     

    :version:
    :author:
    """
    word = "graan"

    def spell_check(word):

        d = enchant.Dict("en_US")
        
        if d.check(word) is False:
            app = QApplication(sys.argv)
            # Create and show the form
            form = Form()
            form.show()
            # Run the main Qt loop
            sys.exit(app.exec_())
           # d.suggest(word)



        """
        @return  :
        @author
        """
        pass


#******************************************************************************

