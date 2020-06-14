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

from PySide2.QtWidgets import QDialog 
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QPushButton

#******************************************************************************

class SetPreferences (QDialog):
    """
    
    :version:
    :author:
    """

    #--------------------------------------------------------------------------
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Set Preferences")

        self.dialogLayout = QVBoxLayout()

        # Setup OK and Cancel buttons
        self.okButton = QPushButton("OK", self)
        self.okButton.pressed.connect(self.on_ok)         
        self.cancelButton = QPushButton("Cancel", self)
        self.cancelButton.pressed.connect(self.on_cancel)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addStretch()
        self.buttonLayout.addWidget(self.okButton)
        self.buttonLayout.addWidget(self.cancelButton)
                      
        self.dialogLayout.addStretch()
        self.dialogLayout.addLayout(self.buttonLayout)

        self.setLayout(self.dialogLayout)
               
        return
        
    #--------------------------------------------------------------------------
      
    def set_tree_defaults(self, treeFont, treeFontSize, iconIndex):
        """ Sets tree parameters in ItemTree instance """
        
        self.treeFont = treeFont 
        self.treeFontSize = treeFontSize
        self.iconIndex = iconIndex
        
        return 
               
    #--------------------------------------------------------------------------  
     
    def get_tree_defaults(self):
        """ Gets existing tree parameters from ItemTree instance """
        
        return (self.treeFont, self.treeFontSize, self.iconIndex)
    
    #--------------------------------------------------------------------------

    def on_ok(self):
        """Handler for ''OK'' button"""
                    
        print("OK button pushed!")
        self.treeFontSize = 24	# test to see if changed value can be returned
        
        self.accept()
        
        return
    
    #--------------------------------------------------------------------------

    def on_cancel(self):
        """Handler for 'Cancel''' button"""
                    
        print("Cancel button pushed!")
        
        self.reject()
        
        return
    
    #--------------------------------------------------------------------------
