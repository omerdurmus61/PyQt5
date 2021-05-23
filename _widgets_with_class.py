import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("First Aplication")
        self.setGeometry(200,20,500,500)
        self.setToolTip("my tooltip")
        self.initUI()


    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Name:")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Surname:")
        self.lbl_surname.move(50,70)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(120,30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(120,70)
        self.txt_surname.resize(200,32)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(120,150)
        self.lbl_result.resize(300,50)
        

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(120,110)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        #print("Name: "+ self.txt_name.text()+"\nSurname: "+self.txt_surname.text())
        self.lbl_result.setText("Name: "+ self.txt_name.text()+" Surname: "+self.txt_surname.text())
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()