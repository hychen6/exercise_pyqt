# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QListView 例子

'''

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5 import QtWidgets
from PyQt5.QtCore import QStringListModel
import sys


class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300, 270)
        layout = QVBoxLayout()

        listView = QListView()  # 创建一个listview对象
        slm = QStringListModel();  # 创建mode
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4']  # 添加的数组数据
        slm.setStringList(self.qList)  # 将数据设置到model
        listView.setModel(slm)  ##绑定 listView 和 model
        listView.clicked.connect(self.clickedlist)  # listview 的点击事件
        layout.addWidget(listView)  # 将list view添加到layout
        self.setLayout(layout)  # 将lay 添加到窗口

    def clickedlist(self, qModelIndex):
        QMessageBox.information(self, "QListView", "你选择了: " + self.qList[qModelIndex.row()])
        print("点击的是：" + str(qModelIndex.row()))

    #点击button “浏览”可以打开对应的文件目录，并将选定的文件目录写入
    #lineEdit文本框内。
    def setBrowerPath(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self,
                                                                   "浏览",
                                                                   "E:\workspace")
        self.lineEdit.setText(download_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())


#第一个问题在界面中显示文件夹中的 py 文件，用 QListWidget 控件，不知道是否合适，有什么需要注意的关键点
#如果要树型结构显示可以左边用一个 QTreeWidget 右边用 QListWidget，点 QTreeWidget 节点信号触发 QListWidget 调用 os.listdir(path)显示目录中文件列表。

#第二个问题，在显示的文件列表中，选定某个 py 文件执行，这个该怎么实现？
#retcode = subprocess.call(["python", full_path_file_name])
#如果要回显结果
#subproc = subprocess.Popen(["python", full_path_file_name], stdout=subprocess.PIPE)
#subproc.stdout.read()

