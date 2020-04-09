import sys
from PyQt5.QtWidgets import (QTextEdit,QAction,qApp,QMainWindow, QToolTip,
    QPushButton, QApplication,QMessageBox,QDesktopWidget,QMenu)
from PyQt5.QtGui import QFont,QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.statusbar=self.statusBar()
        self.statusbar.showMessage('Ready')
##################################菜单栏#################################################################
        #QAction是菜单栏、工具栏或者快捷键的动作的组合。创建了一个图标、一个Exit的标签和一个快捷键组合
        exitAct=QAction(QIcon('exit.jpg'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        #创建了一个状态栏，当鼠标悬停在菜单栏的时候，能显示当前状态。
        exitAct.setStatusTip('Exit application')
        #当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()行为相关联，所以这个动作就能终止这个应用。
        exitAct.triggered.connect(qApp.quit)

        #menuBar()创建菜单栏。这里创建了一个菜单栏，并在上面添加了一个file菜单，并关联了点击退出应用的事件。
        menubar=self.menuBar()
        menubar.setNativeMenuBar(False)
        viewMenu=menubar.addMenu('View')
        viewStatAct=QAction('View statusbar',self,checkable=True)
        viewStatAct.setStatusTip('View Statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)



        fileMenu=menubar.addMenu('&File')
        impMenu=QMenu('Import',self)
        impAct=QAction('Import mail',self)
        impMenu.addAction(impAct)
        newAct = QAction('New', self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)
#########################################################################################
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
#######################################################################################
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        QToolTip.setFont(QFont('SansSerif', 10))
        #提示框
        self.setToolTip('This is a <b>QMainWindow</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())#默认的按钮大小
        btn.move(50, 90)

        qbtn = QPushButton('Quit', self)
        #QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，
        # instance()创建了一个它的实例。
        # QCoreApplication是在QApplication里创建的。
        qbtn.clicked.connect(QCoreApplication.instance().quit)


        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 90)


        #self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.resize(300,300)
        self.center()
        self.show()

    def toggleMenu(self,state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()



    def closeEvent(self, event):
        reply=QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def contextMenuEvent(self, event):
        cmenu=QMenu(self)
        newAct=cmenu.addAction("New")
        opnAct=cmenu.addAction("Open")
        quitAct=cmenu.addAction("Quit")
        #使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action=cmenu.exec_(self.mapToGlobal(event.pos()))

        if action==quitAct:
            qApp.quit()


    def center(self):
        #获得主窗口所在的框架
        qr=self.frameGeometry()
        #获取显示器的分辨率，然后得到屏幕中间点的位置
        cp=QDesktopWidget().availableGeometry().center()
        #把主窗口框架的中心点放置到屏幕的中心位置
        qr.moveCenter(cp)
        #通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了
        self.move(qr.topLeft())




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
