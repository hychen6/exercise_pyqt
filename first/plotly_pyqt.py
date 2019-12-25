#from PyQt5.QtCore import pyqtSlot
#from PyQt5.QtWidgets import QMainWindow

#from Ui_plotly_pyqt import Ui_MainWindow

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from signal_show_main import Ui_MainWindow
import sys


from plotly_py import Plotly_PyQt5

class PlotlyWindow(QMainWindow,Ui_MainWindow):

    def __init__(self,parent=None):
        super(PlotlyWindow,self).__init__(parent)
        self.setupUi(self)
        self.plotly_pyqt5=Plotly_PyQt5(QMainWindow)
        #self.qwebengine.setGeometry(QRect(50,20,1200,600))
        self.webEngineView.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plotly_path_if_hs300_bais()))


app=QApplication(sys.argv)
win=PlotlyWindow()
win.showMaximized()
app.exec_()




