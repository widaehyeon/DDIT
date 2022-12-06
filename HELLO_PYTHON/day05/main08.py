import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./main08.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        start = int(self.le_f.text())
        end = int(self.le_l.text())
        str = "";
        
        for i in range(start,end+1):
            for j in range(0, i):
                str += "*"
            str+="\n";
    
        self.pte.setPlainText(str)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    