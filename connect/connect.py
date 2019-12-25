from connect.test_main import *
from connect.connect import process, process_1
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
import sys

class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui=Ui_MainWindow()
        self.main_ui.setupUi(self)


class childWindow_1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child= process.Ui_Dialog()
        self.child.setupUi(self)

class childWindow_2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child= process_1.Ui_Dialog()
        self.child.setupUi(self)


if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child_1=childWindow_1()
    child_2=childWindow_2()

    btn=window.main_ui.pushButton
    btn_1=window.main_ui.pushButton_2
    btn.clicked.connect(child_1.show)
    btn_1.clicked.connect(child_2.show)

    window.show()
    sys.exit(app.exec_())
