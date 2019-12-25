from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.myButton=QtWidgets.QPushButton(self)
        self.myButton.setObjectName("btn")
        self.myButton.setText("按钮")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        directory1=QFileDialog.getExistingDirectory(
            self,"请选择文件夹","/")
        print(directory1)
        fileName,filetype=QFileDialog.getOpenFileName(
            self,"选择文件","/",directory1,"PNG Files (*.png)")
        print(fileName,filetype)
        files,ok1=QFileDialog.getOpenFileNames(
            self,"多文件选择","/","All Files(*);;Text Files(*.txt)")
        fileName2,ok2=QFileDialog.getSaveFileName(
            self,"文件保存","/","All Files(*);;Text Files(*.txt)")


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())



