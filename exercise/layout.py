import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication,QGridLayout,QLabel,QTextEdit,QLineEdit)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
##############盒布局################################
        hbox = QHBoxLayout()
        #创建一个水平布局，增加两个按钮和弹性空间
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

########################栅格布局#######################
class Example1(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        grid=QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions=[(i,j)for i in range(5) for j in range(4)]
        for position,name in zip(positions,names):

            if name=='':
                continue
            button=QPushButton(name)
            grid.addWidget(button,*position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()

########################制作提交反馈信息的布局##########################
class Example2(QWidget):
    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        #创建标签之间的空间。
        grid.setSpacing(10)

        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)

        grid.addWidget(author,2,0)
        grid.addWidget(authorEdit,2,1)

        grid.addWidget(review, 3, 0)
        #我们可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行显示。
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())