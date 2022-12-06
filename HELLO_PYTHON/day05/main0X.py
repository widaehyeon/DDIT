import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("./main0X.ui")[0]

arr = ['1','2','3','4','5','6','7','8','9']
        


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        for i in range(1,1000):
            rnd = (int)(random.random()*9)
        
            a = arr[0]
            b = arr[rnd]
        
            arr[0] = b
            arr[rnd] = a
        
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        strike = 0
        ball = 0
        str1 = self.te.toPlainText()
        mine = self.le.text()
        mineArr = list(mine)
        
        for i in range(0,3):
            if arr[i]==mineArr[i] :
                strike+=1
            elif arr[i]==mineArr[0] or arr[i]==mineArr[1] or arr[i]==mineArr[2] :
                ball+=1
        print(strike, ball)
        if strike == 3:
            str1="정답입니다."
            QMessageBox.about(self,'call',str1)
        
        if strike != 0 and ball != 0:
            str1 += mine + str(strike) + "S" + str(ball) + "B\n"
        elif strike != 0 and ball == 0:
            str1 += mine + str(strike) + "S" + "OB\n"
        elif strike == 0 and ball != 0:
            str1 += mine + "OS" + str(ball) + "B\n"
        elif strike == 0 and ball == 0:
            str1 += mine + " " + "OSOB\n"
            
        self.te.setText(str1)
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    