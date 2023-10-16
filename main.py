from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QWidget
from PyQt5 import uic

class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui,self).__init__()
        uic.loadUi("MyGui",self)
        self.show()
        self.actionClose.triggered.connect(exit)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.rem)
        info = "info"
        self.label_2 = QLabel(info, self)
        self.label_2.move(100, 150)
        self.label_2.setText('test')
        self.show()



    def add(self):
        global add_sc
        add_sc = self.lineEdit.text()
        add()
        message = QMessageBox()
        message.setText(add_sc + ' has been added.')
        message.exec_()

    def rem(self):
        global rem_sc
        rem_sc = self.lineEdit_2.text()
        remove()
        message = QMessageBox()
        message.setText(rem_sc + ' has been removed.')
        message.exec_()
def remove():

    with open(r"C:\Users\dahpa\Desktop\Open_Application_test.bat", "rt") as bat_file:
        bat_text = bat_file.readlines()
    new_text = []
    for line in bat_text:
        if rem_sc in line:
            continue
        else:
            new_text.append(line)
    with open(r"C:\Users\dahpa\Desktop\Open_Application_test.bat", "wt") as bat_file:
        for line in new_text:
            bat_file.write(line)
def add():
    with open(r"C:\Users\dahpa\Desktop\Open_Application_test.bat", "rt") as bat_file:
        bat_text = bat_file.readlines()
    new_text = []
    for line in bat_text:
            new_text.append(line)
    with open(r"C:\Users\dahpa\Desktop\Open_Application_test.bat", "wt") as bat_file:
        for num in range(1):
            bat_file.write(add_sc + '\n')
            for line in new_text:
                bat_file.write(line)

def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()






if __name__ == '__main__':
    main()