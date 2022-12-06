import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("./main04.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        
        mine = self.le1.text()
        rnd = random.random();
        com = ""
        result = ""
        
        if rnd > 0.5:
            com = "홀" 
        else :
            com = "짝"
            
        if mine == com:
            result = "승리"
        else :
            result = "패배"
            
        self.le2.setText(com)
        self.le3.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    