import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget,QLCDNumber,QSlider,QHBoxLayout,QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        lcd=QLCDNumber(self)
        sld=QSlider(Qt.Vertical,self)

        vbox=QHBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(500,500,500,250)
        self.setWindowTitle('Signal & slot')
        self.show()


if __name__ =='__main__':

    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

