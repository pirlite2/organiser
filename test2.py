import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *



class Setpreference(QDialog):
  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      iconIndex = QLabel('iconIndex')
      treeFont = QLabel('treeFont')
      treeFontSize = QLabel('treeFontSize')
      okButton = QPushButton("OK")
      okButton.pressed.connect(self.on_ok)
      cancelButton = QPushButton("Cancel")
      cancelButton.pressed.connect(self.on_cancel)


      iconIndexbox = QSpinBox()
      treeFontbox = QSpinBox()
      treeFontSizebox = QSpinBox()

      grid = QGridLayout()
      grid.setSpacing(10)

      grid.addWidget(iconIndex, 1, 0)
      grid.addWidget(iconIndexbox, 1, 1)
      iconIndexbox.setValue(30)

      grid.addWidget(treeFont, 2, 0)
      grid.addWidget(treeFontbox, 2, 1)
      treeFontbox.setValue(30)

      grid.addWidget(treeFontSize, 3, 0)
      grid.addWidget(treeFontSizebox, 3, 1)
      treeFontSizebox.setValue(12)

      grid.addWidget(okButton, 4, 0)
      grid.addWidget(cancelButton, 4,1)


      self.setLayout(grid)

      self.setGeometry(500, 500, 500, 300)
      self.setWindowTitle('Setpreference')
      self.show()

  def on_ok(self):
        """Handler for ''OK'' button"""
                    
        print("OK button pushed!")
        #self.iconIndex = self.iconIndexbox.value()
        #self.treefont = self.treeFontbox.value()
        #self.treeFontSize = self.treeFontSizebox.value()	# test to see if changed value can be returned
        
        self.accept()
        
        return
    
    #--------------------------------------------------------------------------

  def on_cancel(self):
        """Handler for 'Cancel''' button"""
                    
        print("Cancel button pushed!")
        
        self.reject()
        
        return

if __name__=="__main__":
  app = QApplication(sys.argv)
  ex = Setpreference()
  sys.exit(app.exec_())
