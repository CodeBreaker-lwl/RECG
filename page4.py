import cv2
from imutils import paths
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog

def init(self):
    self.c9 = 1
    # 载入模板图像

# 信息查看
def openfile_5(self):
    # 获取路径
    global path_openfile_name
    openfile_name = QFileDialog.getOpenFileName(self,'选择文件','',' files(*.txt , *.txt )')
    path_openfile_name = openfile_name[0]
    print("path_openfile_name:",path_openfile_name)
    click(self)

def click(self):
    # 以文本的形式输出到多行文本框
    with open(path_openfile_name,'r',encoding='utf-8') as f:
        msg = f.read()
        self.ui.textEdit_3.setPlainText(msg)

def creat_table_show_5(self):
    if len(path_openfile_name) > 0:
        input_table = pd.read_excel(path_openfile_name)
        input_table_rows = input_table.shape[0]
        input_table_colunms = input_table.shape[1]
        input_table_header = input_table.columns.values.tolist()
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setColumnCount(input_table_colunms)
        self.ui.tableWidget.setRowCount(input_table_rows)
        self.ui.tableWidget.setHorizontalHeaderLabels(input_table_header)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.verticalHeader().setVisible(True)
        for i in range(input_table_rows):
            input_table_rows_values = input_table.iloc[[i]]
            input_table_rows_values_array = np.array(input_table_rows_values)
            input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
            for j in range(input_table_colunms):
                input_table_items_list = input_table_rows_values_list[j]
                input_table_items = str(input_table_items_list)
                newItem = QTableWidgetItem(input_table_items)
                newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                self.ui.tableWidget.setItem(i, j, newItem)
    else:
        print('ok')
        self.ui.centralwidget.show()
        print('fail__2')

def showHead(self,head):
    headlen = len(head)
    for col in range(0, headlen):
        ret = self.excelModel.setHeaderData(col, Qt.Horizontal, head[col])

def showRecord(self,line,lineNO):
    linelen = len(line)
    for col in range(0, linelen):
        if not line[col]:continue
        data = line[col]
        if isinstance(data,float):
            dataInt = int(data)
            if dataInt==data:data = dataInt
            data = str(data)
        item = QStandardItem(data)
        self.excelModel.setItem(lineNO, col, item)

def choose_file_4(self):
    # 批量查看图像
    self.ui.listWidget_2.setViewMode(QListView.IconMode)
    self.ui.listWidget_2.setModelColumn(1)
    self.ui.listWidget_2.itemSelectionChanged.connect(self.onItemSelectionChanged)
    # slider
    self.ui.horizontalSlider_2.valueChanged.connect(self.onSliderPosChanged_9)
    directory9 = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")  # 起始路径
    # 地址设定
    # file_list = os.listdir(directory2)  # 用于返回一个由文件名和目录名组成的列表
    imagePaths_9 = list(paths.list_images(directory9))
    # print("imagePaths:", imagePaths)  # 所有图像路径集合

    # 遍历文件夹
    for (i, imagePath) in enumerate(imagePaths_9):
        img_path = imagePath
        self.image = cv2.imread(img_path, cv2.IMREAD_COLOR)
        self.add_image_thumbnail(self.image, "图片", str(i))  # i是图片顺序

# 清空图像
def clear_img_4(self):
    if self.image.size > 1:
        self.ui.listWidget_2.clear()  # 清除全部
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '已清空')
        msg_box.exec_()
