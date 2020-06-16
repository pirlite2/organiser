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

from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout
from PySide2.QtWidgets import QDialog, QListWidget, QListWidgetItem, QPushButton

#******************************************************************************

class IconPickerDialog(QDialog):
    """
    Dialog for selecting icon
    :version:
    :author: pir
    """

    def __init__(self, iconIndex, treeIconsList):

        super().__init__()

        self.setWindowTitle("Select Icon")

        dialogLayout = QVBoxLayout()

        # Add list widget for icons
        self.listWidget = QListWidget()
        dialogLayout.addWidget(self.listWidget)
        for i in range(0, len(treeIconsList)):
            listWidgetItem = QListWidgetItem(self.listWidget)
            listWidgetItem.setIcon(treeIconsList[i])
        self.listWidget.setCurrentRow(iconIndex)
        
        # Add OK & Cancel buttons
        cancelButton = QPushButton("Cancel")
        cancelButton.pressed.connect(self.on_Cancel)
        okButton = QPushButton("OK")
        okButton.pressed.connect(self.on_OK)
        okCancelLayout = QHBoxLayout()
        okCancelLayout.addStretch()
        okCancelLayout.addWidget(okButton)
        okCancelLayout.addWidget(cancelButton)
        dialogLayout.addLayout(okCancelLayout)
        self.setLayout(dialogLayout)

        self.iconIndex = iconIndex
        self.treeIconsList = treeIconsList

        return

    #--------------------------------------------------------------------------

    def get_icon_index(self):
        
        return self.iconIndex

    #--------------------------------------------------------------------------

    def on_OK(self):

        self.iconIndex = self.listWidget.currentRow()
        self.accept()

        return

    #--------------------------------------------------------------------------

    def on_Cancel(self):
    
        self.reject()

        return

    #--------------------------------------------------------------------------
