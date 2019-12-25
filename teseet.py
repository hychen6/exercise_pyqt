import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication,QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        #提示框
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())#默认的按钮大小
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        #QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，
        # instance()创建了一个它的实例。
        # QCoreApplication是在QApplication里创建的。
        qbtn.clicked.connect(QCoreApplication.instance().quit)


        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()



    def closeEvent(self, event):
        reply=QMessageBox.question(self,'Message',"Are you sure to quit?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
