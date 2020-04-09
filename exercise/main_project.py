from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from signal_show_main import Ui_MainWindow
from PyQt5.QtGui import *
import sys,math
from QfileDialog import MyWindow
from plotly_py import Plotly_PyQt5


class PlotlyWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(PlotlyWindow,self).__init__(parent)

        self.setupUi(self)
        self.plotly_pyqt5=Plotly_PyQt5()
        #self.qwebengine.setGeometry(QRect(50,20,1200,600))
        self.webEngineView.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_if_hs300_bais()))

        #webEngineView不用提升类


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.setupUi(self)
        self.plotly_pyqt5=Plotly_PyQt5()
        #self.qwebengine.setGeometry(QRect(50,20,1200,600))
        self.webEngineView.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_if_hs300_bais()))


        #webEngineView不用提升类

        self.pushButton.clicked.connect(self.msg)

    def paintEvent(self, event):
            # 初始化绘图工具
            qp = QPainter()
            # 开始在窗口绘制
            qp.begin(self)
            # 自定义画点方法
            self.drawPoints(qp)
            # 结束在窗口的绘制
            qp.end()

    def drawPoints(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(1000):
            # 绘制正弦函数图像，它的周期是【-100，100】
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0

            qp.drawPoint(x, y)
        QtWidgets.QApplication.processEvents()
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
        QtWidgets.QApplication.processEvents()
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












if __name__=='__main__':

    app=QApplication(sys.argv)
    while True:
        Button=MainWindow()
        Button.showMaximized()
#        a=Button.msg()
#       print(a)

#        QApplication.processEvents()
#        MainWindow = PlotlyWindow()
 #       MainWindow.showMaximized()
  #      QApplication.processEvents()
        sys.exit(app.exec_())