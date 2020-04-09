import sys
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QSizePolicy,QWidget

from PyQt5 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set=FontProperties(fname='/Users/tatsu/Desktop/PyCharm_project/msyh.ttf')
from  math import pi,sin
import random

import numpy as np


#######FigureCanvas的最终父类是QWidget
class Mydemo(FigureCanvas):
     def __init__(self,parent=None,width=5,height=4,dpi=100):
         #设置中文显示
         #plt.rcParams['font.family']=['Hei']#用来正常显示中文标签
         plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

         ax = plt.gca()
         ax.spines['right'].set_color('none')
         ax.spines['top'].set_color('none')
         ax.xaxis.set_ticks_position('bottom')
         ax.spines['bottom'].set_position(('data', 0))
         ax.yaxis.set_ticks_position('left')
         ax.spines['left'].set_position(('data', 0))

         #新建一个绘制图像
         self.fig=Figure(figsize=(width,height),dpi=dpi)
         self.axes=self.fig.add_subplot(2,1,1)
         self.axes1=self.fig.add_subplot(2,1,2)#画子图，两行一列第二行

         FigureCanvas.__init__(self,self.fig)#初始化画布
         self.setParent(parent)#应用程序可以使用SetParent函数来设置弹出式窗口，层叠窗口或子窗口的父窗口

         FigureCanvas.setSizePolicy(self,
                                    QSizePolicy.Expanding,
                                    QSizePolicy.Expanding)#定义布局策略，使之尽可能填充空间
         FigureCanvas.updateGeometry(self)


     def start_static_plot(self):
            self.fig.suptitle('绘制静态图',fontproperties=font_set)




            t=np.arange(0.0,3.0,0.01)
            s=np.sin(2*pi*t)
            detal_s=(s[2:np.size(s)]-s[1:np.size(s)-1])/(t[2:np.size(t)]-t[1:np.size(t)-1])
            self.axes.plot(t,s)

            self.axes.spines['right'].set_color('none')
            self.axes.spines['top'].set_color('none')
            #self.axes.xaxis.set_ticks_position('bottom')
            self.axes.spines['bottom'].set_position(('data', 0))
            #self.axes.yaxis.set_ticks_position('left')
            self.axes.spines['left'].set_position(('data', 0))
            #self.axes.set_ylabel('静态图：Y轴',fontproperties=font_set)
            self.axes.set_ylabel('静态图：Y轴',fontproperties=font_set)
            #self.axes.set_xlabel('静态图：X轴',fontproperties=font_set)
            self.axes.set_xlabel('静态图：X轴',fontproperties=font_set)
            self.axes.grid(True)

            self.axes1.plot(t[1:np.size(t)-1], detal_s)

            self.axes1.spines['right'].set_color('none')
            self.axes1.spines['top'].set_color('none')
            # self.axes.xaxis.set_ticks_position('bottom')
            self.axes1.spines['bottom'].set_position(('data', 0))
            # self.axes.yaxis.set_ticks_position('left')
            self.axes1.spines['left'].set_position(('data', 0))
            # self.axes.set_ylabel('静态图：Y轴',fontproperties=font_set)
            self.axes1.set_ylabel('dong态图：Y轴', fontproperties=font_set)
            # self.axes.set_xlabel('静态图：X轴',fontproperties=font_set)
            self.axes1.set_xlabel('dong态图：X轴', fontproperties=font_set)
            self.axes1.grid(True)

     def start_dynamic_plot(self,*args,**kwargs):
            timer=QtCore.QTimer(self)
            timer.timeout.connect(self.update_figure)
            self.axes1.spines['right'].set_color('none')
            self.axes1.spines['top'].set_color('none')
            self.axes1.spines['bottom'].set_position(('data', 0))
            self.axes1.spines['left'].set_position(('data', 0))
            self.axes1.set_ylabel('动态图：Y轴', fontproperties=font_set)
            self.axes1.set_xlabel('动态图：X轴', fontproperties=font_set)

            timer.start(1000)

     def update_figure(self):
            self.fig.suptitle('测试动态图',fontproperties=font_set)
            l=[random.randint(0,10)for i in range(4)]
            self.axes1.plot([0,1,2,3],l,'r')

            self.axes1.grid(False)
            self.draw()

class MatplotlibWidget(QWidget):
    def __init__(self,parent=None):
        super(MatplotlibWidget,self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout=QVBoxLayout(self)
        self.mpl=Mydemo(self,width=5,height=4,dpi=100)
        self.mpl.start_static_plot()
        #self.mpl.start_dynamic_plot()
        #self.mpl_ntb=NavigationToolbar(self.mpl,self)

        self.layout.addWidget(self.mpl)
        #self.layout.addWidget(self.mpl_ntb)


if __name__=='__main__':
    app=QApplication(sys.argv)
    ui=MatplotlibWidget()
    #ui.mpl.start_dynamic_plot()
    ui.show()
    sys.exit(app.exec_())
        
    



