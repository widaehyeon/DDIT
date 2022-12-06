import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./main01.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        print("버튼이 클릭되었습니다.")
        self.lbl.setText("Good Evening")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    