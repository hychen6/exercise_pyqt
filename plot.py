import matplotlib
import sys,math
import pandas as pd









matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set=FontProperties(fname='/Users/tatsu/Desktop/PyCharm_project/msyh.ttf')

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


from signal_show_main import Ui_MainWindow


from  math import pi

import numpy as np

class Mydemo(FigureCanvas):
    def __init__(self, parent=None, width=30, height=24, dpi=200):

        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.style.use('classic')





        # 新建一个绘制图像
        self.fig,self.ax= plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(width,height))
        self.fig.subplots_adjust(left=0.1, right=0.99, bottom=0.07, top=0.95, hspace = 0 )



        #self.axes = self.fig.add_subplot(2, 1, 1)
        #self.axes1 = self.fig.add_subplot(2, 1, 2)  # 画子图，两行一列第二行

        FigureCanvas.__init__(self, self.fig)  # 初始化画布
        self.setParent(parent)  # 应用程序可以使用SetParent函数来设置弹出式窗口，层叠窗口或子窗口的父窗口

        #FigureCanvas.setSizePolicy(self,
        #                          QSizePolicy.Expanding,
        #                          QSizePolicy.Expanding)  # 定义布局策略，使之尽可能填充空间

        FigureCanvas.updateGeometry(self)



    def start_static_plot(self):
        self.fig.suptitle('绘制静态图', fontproperties=font_set)

        file = PushBottom.msg(self)

        df = pd.read_excel(file)

        a = np.array(df['t'])
        s = np.array(df['sint'])
        detal_s = (s[2:np.size(s)] - s[1:np.size(s) - 1]) / (a[2:np.size(a)] - a[1:np.size(a) - 1])
        detal_a = a[1:np.size(a) - 1]


        self.axes=self.ax[0]

        self.axes.plot(a,s)
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.spines['bottom'].set_position(('data', 0))
        self.axes.yaxis.set_ticks_position('left')
        self.axes.spines['left'].set_position(('data', 0))
        self.axes.spines['right'].set_color('none')
        self.axes.spines['top'].set_color('none')
        self.axes.spines['bottom'].set_position(('data', 0))
        self.axes.spines['left'].set_position(('data', 0))
        self.axes.set_ylabel('Y', fontproperties=font_set)
        self.axes.set_xlabel('X', fontproperties=font_set)
        self.axes.grid(True)



        self.axes1=self.ax[1]
        self.axes1.plot(detal_a, detal_s)
        self.axes1.spines['right'].set_color('none')
        self.axes1.spines['top'].set_color('none')
        self.axes1.spines['bottom'].set_position(('data', 0))
        self.axes1.spines['left'].set_position(('data', 0))
        self.axes1.set_ylabel('dY/dX', fontproperties=font_set)
        self.axes1.set_xlabel('X', fontproperties=font_set)
        self.axes1.grid(True)

        #self.fig.subplots_adjust(hspace=0.5)






class MatplotlibWidget(QWidget):
    def __init__(self,parent=None):
        super(MatplotlibWidget,self).__init__(parent)
        self.initUi()



    def initUi(self):
        self.layout=QVBoxLayout(self)
        self.mpl=Mydemo(self,width=14.55,height=10.8,dpi=100)
        self.mpl.start_static_plot()


class PushBottom(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(PushBottom, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.refresh)

    def refresh(self):
        self.setupUi(self)
        self.pushButton.clicked.connect(self.refresh)

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
#####################################################################
class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing,self).__init__(parent)
        self.resize(300,200)
        self.setWindowTitle('在窗口画点')

    def paintEvent(self,event):
        #初始化绘图工具
        qp=QPainter()
        #开始在窗口绘制
        qp.begin(self)
        #自定义画点方法
        self.drawLines1(qp)

        # 结束在窗口的绘制
        qp.end()

    def drawLines1(self, qp):
        pen = QPen(Qt.darkBlue, 1.0, Qt.SolidLine)


        pen.setStyle(Qt.DashLine)
        qp.setPen(pen)
        qp.drawLine(250, 47, 250, 805)
        qp.drawLine(124,500,1160,500)

    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        size=self.size()

        for i in range(1000):
            #绘制正弦函数图像，它的周期是【-100，100】
            x=100*(-1+2.0*i/1000)+size.width()/2.0
            y=-50*math.sin((x-size.width()/2.0)*math.pi/50)+size.height()/2.0

            qp.drawPoint(x,y)



if __name__=='__main__':
    app=QApplication(sys.argv)
    MainWindow=PushBottom()
    #ui=signal_show_main.Ui_MainWindow()
    #ui.widget=MatplotlibWidget()
    #ui.setupUi(MainWindow)
    #ui.mpl.start_dynamic_plot()
    MainWindow.show()
    sys.exit(app.exec_())