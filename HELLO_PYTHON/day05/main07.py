import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

form_class = uic.loadUiType("./main07.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        self.le1.returnPressed.connect(self.btnClick)
        
    def btnClick(self):
        
        mine = self.le1.text()
        rnd = random.random();
        com = ""
        result = ""
        
        if rnd > 0.66:
            com = "가위" 
        elif rnd > 0.33:
            com = "바위"
        else :
            com = "보" 
            
        if mine == com:
            result = "무승부"
        elif mine == "가위" and com == "보" or mine == "바위" and com == "가위" or mine == "보" and com == "바위":
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    