import sys
from PyQt5 import QtCore,QtWidgets,QtGui
#import untitled



class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        #添加菜单栏
        file_menu=QtWidgets.QMenuBar(self)#实例化一个菜单栏
        file_menu.setFixedWidth(200)
        file_menu.addMenu("文件")
        file_menu.addMenu("编辑")
        file_menu.addMenu("关于")


        #添加工具栏
        view_toolbar=self.addToolBar("view")
        view_toolbar.addAction("打开")
        view_toolbar.addAction("保存")
        view_toolbar.addAction("撤回")

        #状态栏，要先将主窗口的状态栏赋值给一个变量
        status=self.statusBar()
        status.showMessage("这是一个状态栏消息")

        #中央控件，每一个主窗口都会有一个中央控件，就算其是一个占位符，也必须存在。
        pushbotton=QtWidgets.QWidget()
        self.setCentralWidget(pushbotton)


class LayoutApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget=QtWidgets.QWidget()#实例化一个widget控件
        main_layout=QtWidgets.QHBoxLayout()#水平布局层,垂直布局层QVBoxLayout
        main_widget.setLayout(main_layout)# 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1=QtWidgets.QPushButton('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        # 将按钮添加到水平布局中
        main_layout.addWidget(button_1)
        main_layout.addWidget(button_2)
        main_layout.addWidget(button_3)

        self.setCentralWidget(main_widget)


class LayoutApp_1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        main_widget=QtWidgets.QWidget()
        main_layout=QtWidgets.QFormLayout()  # 实例化一个垂直布局层
        main_widget.setLayout(main_layout)

        button_1=QtWidgets.QLabel('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        button_4 = QtWidgets.QPushButton('按钮四')

        # 将按钮添加到水平布局中
        main_layout.addRow(button_1,button_2)
        main_layout.addRow(button_3)
        main_layout.addWidget(button_4)

        self.setCentralWidget(main_widget)


class ButtonApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setWindowTitle("Qt For Python按钮控件")
        self.setFixedSize(500,200)
        self.main_widget=QtWidgets.QWidget()
        self.main_layput=QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_layput)

        self.btn_1=QtWidgets.QPushButton("按钮一",self)

        self.btn_2=QtWidgets.QPushButton(self)
        self.btn_2.setText("按钮二")
        self.btn_2.setFixedSize(487,40)
        #self.btn_2.clicked.connect(self.clicks) # 连接点击信号到响应方法

        self.btn_2.clicked.connect(self.clicks)


        self.btn_3=QtWidgets.QPushButton("按钮三",self)
        icon_img=QtGui.QIcon("./zhu.png")
        self.btn_3.setIcon(icon_img)
        self.btn_3.setEnabled(False)

        self.main_layput.addWidget(self.btn_1)
        self.main_layput.addWidget(self.btn_2)
        self.main_layput.addWidget(self.btn_3)

        self.statusBar()

        self.setCentralWidget(self.main_widget)

        self.show()


    def clicks(self):

        gui = ButtonApp()
        gui.close()
        bnt_2gui = LayoutApp_1()
        bnt_2gui.show()
        print("Botton 2 was pressed!")


    def buttonClicked(self):

        sender=self.sender()
        self.statusBar().showMessage(sender.text() + 'was pressed')
        bnt_2gui = LayoutApp_1()
        bnt_2gui.show()



def main():



    app=QtWidgets.QApplication(sys.argv)
    gui=ButtonApp()
    gui.show()



    sys.exit(app.exec_())


if __name__=='__main__':
    main()