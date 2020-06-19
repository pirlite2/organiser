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

from PySide2.QtCore import QDate, QTime, QDateTime

from PySide2.QtWidgets import QDialog, QLabel, QCheckBox
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QPushButton, QLineEdit, QDateTimeEdit 

from IconPickerButton import IconPickerButton
from ISO8601_Support import iso8601_to_tuple, tuple_to_iso8601

#******************************************************************************

class EditTaskItem (QDialog):
    """
    Dialog box to edit task item
    :version:
    :author: pir
    """
  
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
        iconLabel = QLabel("Icon:")
        iconTitleLayout.addWidget(iconLabel)

        self.iconButton = IconPickerButton(self.iconIndex, self.treeIconsList)
        
        iconTitleLayout.addWidget(self.iconButton)
        iconTitleLayout.addStretch()
        titleLabel = QLabel("Title:")
        iconTitleLayout.addWidget(titleLabel)
        self.titleEditor = QLineEdit()
        self.titleEditor.setText(title)
        iconTitleLayout.addWidget(self.titleEditor)

        # Add schedule setting
        dateTimeLayout = QHBoxLayout()
        dateTimeLayout.addStretch()

        self.deadlineCheckBox = QCheckBox("Set deadline?")
        dateTimeLayout.addWidget(self.deadlineCheckBox)
        self.deadlineCheckBox.stateChanged.connect(self.on_checkbox_changed)

        if (self.deadline != 0):
            self.deadlineCheckBox.setChecked(True)
            (hours, minutes, day, month, year) = iso8601_to_tuple(self.deadline) 
            deadlineDateTime = QDateTime(QDate(year, month, day), QTime(hours, minutes))
            self.dateTimeEditControl = QDateTimeEdit(deadlineDateTime)
            self.dateTimeEditControl.setEnabled(True)
        else:
            self.deadlineCheckBox.setChecked(False)
            self.dateTimeEditControl = QDateTimeEdit(QDateTime.currentDateTime())
            self.dateTimeEditControl.setEnabled(False)
        
        self.dateTimeEditControl.setCalendarPopup(True)
        self.dateTimeEditControl.setDisplayFormat("hh:mm @ dd-MMM-yyyy")

        dateTimeLayout.addWidget(self.dateTimeEditControl)
        dateTimeLayout.addStretch()
      
        # Setup OK and Cancel buttons
        okButton = QPushButton("OK", self)
        okButton.pressed.connect(self.on_ok)         
        cancelButton = QPushButton("Cancel", self)
        cancelButton.pressed.connect(self.on_cancel)
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
                      
        dialogLayout = QVBoxLayout()
        dialogLayout.addLayout(iconTitleLayout)
        dialogLayout.addStretch()
        dialogLayout.addLayout(dateTimeLayout)
        dialogLayout.addStretch()   
        dialogLayout.addLayout(buttonLayout)

        self.setLayout(dialogLayout)
        self.titleEditor.setFocus()
               
        return
        
    #--------------------------------------------------------------------------
   
    def get_item_values(self):
        """ Returns existing tree parameters to ItemTree instance """
        
        return (self.iconIndex, self.title, self.deadline)
    
    #--------------------------------------------------------------------------

    def on_ok(self):
        """ Handler for EditTaskitem 'OK' button """
                          
        # Get/update values from controls
        self.iconIndex = self.iconButton.get_icon_index()
        self.title = self.titleEditor.text()       

        # Get deadline from dataTimeEditControl
        if (self.deadlineCheckBox.isChecked()):
            # Extract deadline
            date = self.dateTimeEditControl.date()
            time = self.dateTimeEditControl.time()
            dateTimeTuple = (time.hour(), time.minute(), date.day(), date.month(), date.year())
            self.deadline = tuple_to_iso8601(dateTimeTuple)
        else:
            # No deadline set
            self.deadline = 0

        self.accept()
        
        return
    
    #--------------------------------------------------------------------------

    def on_cancel(self):
        """Handler for EditTaskitem 'Cancel' button"""
                          
        self.reject()
        
        return
    
    #--------------------------------------------------------------------------

    def on_checkbox_changed(self, state):
        """ Handler for self.deadlineCheckBox """
        
        # Toggle check box state
        checkBoxState = self.deadlineCheckBox.isChecked()
        self.dateTimeEditControl.setEnabled(checkBoxState)

        return

#******************************************************************************
