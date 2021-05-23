import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import  QIcon

def labels(win):
    label1 = QtWidgets.QLabel(win)

    label1.setText("Ord.Prof. Ömer DURMUŞ ")
    label1.move(250,200)

    #label2 = QtWidgets.QLabel(win)
    #label2.setPixmap(QtGui.QPixmap("logo1.png"))
    #label2.move(200,60)

def clicked():
    print("OK")

def button(win):
    btn1 = QtWidgets.QPushButton(win)
    btn1.setText("click")
    btn1.move(250,250)
    btn1.clicked.connect(clicked)



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Aplication")
    
    win.setGeometry(200,20,500,500)
    win.setWindowIcon(QIcon("logo1.png"))

    labels(win)
    button(win)    

    win.show()

    sys.exit(app.exec_())




window()


