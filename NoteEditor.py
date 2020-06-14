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
from PySide2.QtWidgets import QTextEdit

#******************************************************************************

class NoteEditor(QTextEdit):
    """ 
    :version:
    :author:
    """

    #--------------------------------------------------------------------------
    
    def __init__(self):
        super().__init__()
        
        return

    #--------------------------------------------------------------------------

    def setTextDocument(self, document):
        """
        Set document of the text editor
        :version:
        :author:
        """

        self.setDocument(document)

        return

#******************************************************************************
