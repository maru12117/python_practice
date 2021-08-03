#Demoform

'''import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("DemoForm.ui")[0]

class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 PyQt 데모")

if __name__=="__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()'''

#버튼 사용

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Mainform.ui")[0] #.ui를 가져오는 공통

class DemoForm(QMainWindow, form_class): #QMainWindow은 설정시 가져오는 것
    def __init__(self): #스타트 UI
        super().__init__()
        self.setupUi(self)
        self.label.setText("버튼을 클릭해주세요!") #라벨에..출력함
    def FirstClick(self):   #버튼했을때 click()하면 FirstClick() 함수로 이동
        self.label.setText("첫번째 버튼을 클릭")
    def SecondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def ThirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

if __name__=="__main__": #공통
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
