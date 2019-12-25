import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from functools import partial
from connect import process
from convert import converse_main as convert_main


def convert(ui):

    [a,b]=[ui.lineEdit.text(),ui.lineEdit_2.text()]

    if a =='' and b =='':
        result_1="请输入数字"
        ui.lineEdit.setText(str(result_1))
        QApplication.processEvents()
    else:
        if(b is '') or (a is not '' and b is not ''):
            input=a
            result=float(input)*6.7
            ui.lineEdit_2.setText(str(result))
            QApplication.processEvents()
        if a is '':
            input_1=b
            result_1 = float(input_1) / 6.7
            ui.lineEdit.setText(str(result_1))
            QApplication.processEvents()

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child= process.Ui_Dialog()
        self.child.setupUi(self)



if __name__=='__main__':
    app=QApplication(sys.argv)
    while True:
        MainWindow=QMainWindow()


        ui=convert_main.Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.pushButton.clicked.connect(partial(convert,ui))


        child=childWindow()
        ui.pushButton_2.clicked.connect(child.show)
        MainWindow.show()
        QApplication.processEvents()
        exit(app.exec_())