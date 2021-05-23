import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

def window():
    app = QApplication(sys.argv)
    clear = QtWidgets.QPushButton("clear")
    update = QtWidgets.QPushButton("update")
    
    """
    hbox = QtWidgets.QHBoxLayout()
    hbox.addStretch()
    hbox.addWidget(clear)
    hbox.addWidget(update)
    """


    vbox = QtWidgets.QVBoxLayout()
    vbox.addStretch()
    vbox.addWidget(clear)
    vbox.addWidget(update)

    win = QtWidgets.QWidget()
    win.setWindowTitle("Horizontal Layout")
    win.setLayout(vbox)
    win.setGeometry(200,200,450,200)
    win.show()

    sys.exit(app.exec_()),

window()

