import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Number 1:")
        self.lbl_num1.move(50,30)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.move(150,30)
        self.txt_num1.resize(200,32)


        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Number 2:")
        self.lbl_num2.move(50,80)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.move(150,80)
        self.txt_num2.resize(200,32)

        self.btn_sum = QtWidgets.QPushButton(self)
        self.btn_sum.setText("Sum")
        self.btn_sum.move(150,130)
        self.btn_sum.clicked.connect(self.calculate)

        self.btn_subtract = QtWidgets.QPushButton(self)
        self.btn_subtract.setText("subtract")
        self.btn_subtract.move(150,170)
        self.btn_subtract.clicked.connect(self.calculate)

        self.btn_multiplication = QtWidgets.QPushButton(self)
        self.btn_multiplication.setText("multiplication")
        self.btn_multiplication.move(250,130)
        self.btn_multiplication.clicked.connect(self.calculate)


        self.btn_divide = QtWidgets.QPushButton(self)
        self.btn_divide.setText("divide")
        self.btn_divide.move(250,170)
        self.btn_divide.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result: ")
        self.lbl_result.move(150,200)


    def calculate(self):
        #sender returns wich button clicked
        sender = self.sender().text()

        result = 0
        if sender == "Sum":
            result =  int(self.txt_num1.text()) + int(self.txt_num2.text()) 
        elif sender == "subtract":
            result =  int(self.txt_num1.text()) - int(self.txt_num2.text()) 
        elif sender == "multiplication":
            result =  int(self.txt_num1.text()) * int(self.txt_num2.text()) 
        elif sender == "divide":
            result =  int(self.txt_num1.text()) / int(self.txt_num2.text()) 
            
        self.lbl_result.setText(f"Result: {result}")

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()