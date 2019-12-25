from PyQt5 import QtWidgets
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QFileDialog,QMainWindow
from signal_show_main import Ui_MainWindow
#from plotly_py import Plotly_PyQt5

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.msg)
        #self.plotly_pyqt5 = Plotly_PyQt5()
        #self.webEngineView.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_if_hs300_bais()))

    def msg(self):
        '''
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "C:/")  # 起始路径
        print(directory1)
        '''

#        fileName1, filetype = QFileDialog.getOpenFileName(self,
#                                                          "选取文件",
#                                                          "C:/",
#                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                                  "选取文件",
                                                                  "C:/",
                                                                  "All Files (*)")
        print(fileName1)

        return fileName1
        '''
        files, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "C:/",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files, ok1)

        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "C:/",
                                                     "All Files (*);;Text Files (*.txt)")
        '''





'''
class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.myButton = QtWidgets.QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "C:/")  # 起始路径
        print(directory1)

        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "C:/",
                                                          "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)

        files, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "C:/",
                                                  "All Files (*);;Text Files (*.txt)")
        print(files, ok1)

        fileName2, ok2 = QFileDialog.getSaveFileName(self,
                                                     "文件保存",
                                                     "C:/",
                                                     "All Files (*);;Text Files (*.txt)")

'''
'''
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
'''

