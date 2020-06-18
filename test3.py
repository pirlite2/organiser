import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class FontDialogDemo(QDialog):
    def __init__(self,parent=None):
        super(FontDialogDemo,self).__init__(parent)
        layout=QVBoxLayout()
        
        self.fbtn=QPushButton("Treefont change")
        self.fbtn.clicked.connect(self.getFont)
        layout.addWidget(self.fbtn)
        self.setLayout(layout)
        self.setWindowTitle("TreeFont Dialog")


    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.fle.setFont(font)
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=FontDialogDemo()
    win.show()
    sys.exit(app.exec_())
