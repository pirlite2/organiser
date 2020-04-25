#! /usr/bin/env python3

# Example Qt dialog -- pir -- 24.4.2020

#******************************************************************************
# Insert licence here!



#******************************************************************************

from sys import exit
from PySide2.QtWidgets import QDialog
from PySide2.QtWidgets import QPushButton

from PySide2.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget 

#******************************************************************************

class ExampleDialog(QDialog):
    def __init__(self, dialogTitle):
        super().__init__()
        
        self.setWindowTitle(dialogTitle)

        self.pushButton = QPushButton("Push to close dialog", self)
        self.pushButton.pressed.connect(self.on_push)
		        
        self.dialogLayout = QVBoxLayout()
        self.dialogLayout.addStretch()
        self.dialogLayout.addWidget(self.pushButton)
        self.dialogLayout.addStretch()

        self.setLayout(self.dialogLayout)
        self.exec_()	# Not sure why this still has to have a trailing underscore?
        
    #--------------------------------------------------------------------------
    
    def on_push(self):
        """Handler for button push"""
        print("button pushed!")
        self.close()
        
        return
        
#******************************************************************************

# Main program
if __name__ == "__main__":
    application = QApplication([])

    mainWindow = QMainWindow()
    mainWindow.setWindowTitle("test harness")
    
    exampleDialog = ExampleDialog("testing ExampleDialog")
    mainWindow.setCentralWidget(exampleDialog) 
    mainWindow.show()

    exit(application.exec_())   # Not sure why this has to be `exec_` with a trailing underscore?

#******************************************************************************
