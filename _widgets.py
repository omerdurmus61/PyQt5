import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("First Aplication")
    win.setGeometry(200,20,500,500)
    
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Name:")
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Surname:")
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(120,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(120,70)

    def clicked(self):
        print("Name: "+ txt_name.text()+"\nSurname: "+txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Save")
    btn_save.move(120,110)
    btn_save.clicked.connect(clicked)


    win.show()
    sys.exit(app.exec_())

window()

