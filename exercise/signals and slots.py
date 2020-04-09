#事件和信号

#事件


#所有的应用都是事件驱动的。事件大部分都是由用户的行为产生的，当然也有其他的事件产生方式，比如网络的连接，窗口管理器或者定时器等。
# 调用应用的exec_()方法时，应用会进入主循环，主循环会监听和分发事件。

#在事件模型中，有三个角色：

#事件源
#事件
#事件目标
#事件源就是发生了状态改变的对象。事件是这个对象状态改变的内容。事件目标是事件想作用的目标。事件源绑定事件处理函数，然后作用于事件目标身上。

#PyQt5处理事件方面有个signal and slot机制。Signals and slots用于对象间的通讯。事件触发的时候，发生一个signal，slot是用来被Python调用的
# （相当于一个句柄？这个词也好恶心，就是相当于事件的绑定函数）slot只有在事件触发的时候才能调用。


import sys
from PyQt5.QtCore import Qt,pyqtSignal,QObject
from PyQt5.QtWidgets import (QPushButton,QMainWindow,QWidget,QLCDNumber,QSlider,QVBoxLayout,QApplication,QGridLayout,QLabel)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd=QLCDNumber(self)
        sld=QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)
#
        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()

######################重构事件处理器##################################
######按下esc键退出

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

######################事件对象#####################################
class Example1(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        x=0
        y=0
        self.text="x:{0},y:{1}".format(x,y)
        self.label=QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x=e.x()
        y=e.y()

        text="x:{0}, y:{1}".format(x,y)
        self.label.setText(text)

###########################事件发送#####################################
#有时候我们会想知道是哪个组件发出了一个信号，PyQt5里的sender()方法能搞定这件事。
class Example2(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
######################信号发送#################################
#QObject实例能发送事件信号。下面的例子是发送自定义的信号。

#我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定。
#Communicate类创建了一个pyqtSignal()属性的信号。
class Communicate(QObject):

    closeApp=pyqtSignal()

class Example3(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #closeApp信号QMainWindow的close()方法绑定。
        self.c=Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()
    #点击窗口的时候，发送closeApp信号，程序终止。
    def mousePressEvent(self, event):

        self.c.closeApp.emit()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example3()
    sys.exit(app.exec_())

