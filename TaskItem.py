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
from PySide2.QtWidgets import QTreeWidgetItem

#******************************************************************************

class TaskItem (QTreeWidgetItem):
    """
    Sub-classed QTreeWidgetItem 

    :version:
    :author: pir
    """

    #--------------------------------------------------------------------------
    
    def __init(self):
        super.__init__()
        
    def attributes(self, deadline, icon):
        # Define attributes
        self.note = QTextDocument()
        self.deadline = deadline
        #self.iconIndex = iconIndex  # TODO - add this to store actual icon index - required for editing!
        self.icon = icon
        
        return
           
#******************************************************************************


