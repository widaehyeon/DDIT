import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./main06.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        dan = int(self.le.text())
        str = ''
        str+= "{}*1={}\n".format(dan,dan*1)
        str+= "{}*2={}\n".format(dan,dan*2)
        str+= "{}*3={}\n".format(dan,dan*3)
        str+= "{}*4={}\n".format(dan,dan*4)
        str+= "{}*5={}\n".format(dan,dan*5)
        str+= "{}*6={}\n".format(dan,dan*6)
        str+= "{}*7={}\n".format(dan,dan*7)
        str+= "{}*8={}\n".format(dan,dan*8)
        str+= "{}*9={}\n".format(dan,dan*9)
        
        self.te.setText(str)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    