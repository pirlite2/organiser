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

from PySide2.QtWidgets import QDialog, QLabel
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QPushButton, QLineEdit

#******************************************************************************

class EditTaskItem (QDialog):
    """
    Dialog box to edit task item
    :version:
    :author: pir
    """

    #--------------------------------------------------------------------------
    
    def __init__(self, iconIndex, title, deadline, treeIconsList):
        super().__init__()
        
        self.setWindowTitle("Edit Task Item")

        self.iconIndex = iconIndex
        self.title = title
        self.deadline = deadline
        self.treeIconsList = treeIconsList

        # Setup icon & title layout
        iconTitleLayout = QHBoxLayout()
        iconTitleLayout.addStretch()
        iconLabel = QLabel("Icon")
        iconTitleLayout.addWidget(iconLabel)
        self.iconButton = QPushButton()
        self.iconButton.setIcon(treeIconsList[iconIndex])
        iconTitleLayout.addWidget(self.iconButton)
        iconTitleLayout.addStretch()
        titleLabel = QLabel("Title")
        iconTitleLayout.addWidget(titleLabel)
        self.titleEditor = QLineEdit()
        self.titleEditor.setText(title)
        iconTitleLayout.addWidget(self.titleEditor)

        # Add schedule setting
        #TODO


      
        # Setup OK and Cancel buttons
        self.okButton = QPushButton("OK", self)
        self.okButton.pressed.connect(self.on_ok)         
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.pressed.connect(self.on_cancel)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(self.okButton)
        self.buttonLayout.addWidget(self.cancelButton)
                      
        self.dialogLayout = QVBoxLayout()
        self.dialogLayout.addLayout(iconTitleLayout)
        self.dialogLayout.addStretch()
        self.dialogLayout.addLayout(self.buttonLayout)

        self.setLayout(self.dialogLayout)
        self.titleEditor.setFocus()
               
        return
        
    #--------------------------------------------------------------------------
   
    def get_item_values(self):
        """ Returns existing tree parameters to ItemTree instance """
        
        return (self.iconIndex, self.title, self.deadline)
    
    #--------------------------------------------------------------------------

    def on_ok(self):
        """Handler for 'OK' button"""
                    
        #print("OK button pushed!")
        
        # Get/update values from controls
        self.iconIndex = 0
        self.deadline = 123
        self.title = self.titleEditor.text()       
        self.accept()
        
        return
    
    #--------------------------------------------------------------------------

    def on_cancel(self):
        """Handler for 'Cancel' button"""
                    
        print("Cancel button pushed!")
        
        self.reject()
        
        return
    
    #--------------------------------------------------------------------------
