#******************************************************************************
# Insert licence here!



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
