from datetime import datetime
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
global img
global point1, point2
import time
import numpy as np
import os
from paddleocr import PaddleOCR, draw_ocr
import cv2
from PIL import Image

# 保存图像
def saveimg(self):
    if self.img.size>1:
        fileName, tmp = QFileDialog.getSaveFileName(self, '保存图像', str(self.fname)+'_fin', '*.png *.jpg *.bmp')
        if fileName == '':
            return
        print(fileName)
        root_dir, file_name = os.path.split(fileName)  # 按照路径将文件名和路径分割开
        pwd = os.getcwd()  # 返回当前工作目录
        if root_dir:
            os.chdir(root_dir)  # 改变当前工作目录到指定的路径。
        # 保存图像

        cv2.imwrite(file_name, self.img_save)
        os.chdir(pwd)
        # 打印处理结果
        dt = datetime.now()
        now_time = dt.strftime("%Y-%m-%d %H:%M:%S")  # 打印当前时间
        text = now_time + "保存图像完成：" + '\n'
        self.ui.textEdit.append(text)
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '图像为空，无法保存  ')
        msg_box.exec_()

# 图像识别
def image_recognition(self):
    if self.img.size>1:
        now = time.localtime()
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
        result = ocr.ocr(self.fileName, cls=True)
        print("result",result)
        for line in result:
            print(line)

        image = Image.open(self.fileName).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        #print("boxes1:",boxes)
        #print("txts:",txts)
        #print("scores:",scores)
        nowt = time.strftime("%Y-%m-%d-%H_%M_%S", now)  # 这一步就是对时间进行格式化
        image_recognition_results = "number: " + str(txts) + "； " + "scores: " + str(scores)
        a = os.path.split(self.fileName)[-1]
        image_recognition_results1 = a + " " + str(txts) + " " + str(scores)
        with open('data_recognition_result_saving/save_data/result.txt', 'a', encoding='utf-8') as f:
               f.write(image_recognition_results1 + '\n')

        self.ui.textEdit.append("识别结果："+nowt+image_recognition_results)
        im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
        print("boxes2:",boxes)
        self.img_save = im_show
        QtImg = cvImgtoQtImg(im_show)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_11.width(), self.ui.label_11.height())  # 设置图片大小
        self.ui.label_11.setPixmap(jpg_out_gray)  # 设置图片显示

    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '请选择图像  ')
        msg_box.exec_()

def select_button_clicked(self):
    self.fileName, tmp = QFileDialog.getOpenFileName(self, '打开图像', 'Image', '*.png *.jpg *.bmp *.jpeg')
    print(self.fileName)
    if self.fileName == '':
        return
    root_dir, file_name = os.path.split(self.fileName)  # 按照路径将文件名和路径分割开
    pwd = os.getcwd()  # 返回当前工作目录
    if root_dir:
        os.chdir(root_dir)  # 改变当前工作目录到指定的路径。
    self.img = cv2.imread(file_name, -1)
    os.chdir(pwd)
    if self.img.size <= 1:
        return
    self.fname = file_name.split('.')[0]
    self.imgOrg = self.img.copy()
    if len(self.img.shape) == 3:
        self.c = self.img.shape[2]
        if self.img.shape[2] == 4:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGRA2BGR)

    # 显示图片到界面
    self.imgShow = self.img
    self.h = self.imgShow.shape[0]
    self.w = self.imgShow.shape[1]
    self.ui.textBrowser.setText('%s×%s×%s' % (self.w, self.h, self.c))

    # 图像放射：清空坐标点
    point_clease = self.point
    if point_clease :
       self.point = []
       print("已清空坐标！")
    # ------显示图片到标签label_10------
    QtImg = cvImgtoQtImg(self.img)
    jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_10.width(), self.ui.label_10.height())  # 设置图片大小
    self.ui.label_10.setPixmap(jpg_out_gray)  # 设置图片显示


# 10-清空数据
def clear(self):
    self.img = np.ndarray(())
    self.imgOrg = np.ndarray(())
    self.imgShow = np.ndarray(())
    self.image_cut = np.ndarray(())
    self.w = 0
    self.h = 0
    self.c = 1
    self.ui.textBrowser.setText('')
    self.ui.textBrowser_4.setText('')
    self.ui.label_10.setPixmap(QtGui.QPixmap(""))
    self.ui.label_11.setPixmap(QtGui.QPixmap(""))
    # 打印处理结果
    dt = datetime.now()
    now_time = dt.strftime("%Y-%m-%d %H:%M:%S")  # 打印当前时间
    text = now_time + "清空数据完成：" + '\n'
    self.ui.textEdit.append(text)

# 11-重置图像
def reset(self):
    if self.img.size>1:
        self.img = self.imgOrg
        refreshShow1(self)
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '请选择图像  ')
        msg_box.exec_()

# 11-2显示图像
def refreshShow1(self):
    if self.img.size > 1:
        img1 = self.img.copy()
        QtImg = cvImgtoQtImg(img1)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_11.width(), self.ui.label_11.height())  # 设置图片大小
        self.ui.label_11.setPixmap(jpg_out_gray)  # 设置图片显示
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '请选择图像  ')
        msg_box.exec_()


# 导出图像数据
def showlarge(self):
    if self.img.size>1:
        cv2.imshow('Original pic',self.img)
        cv2.setMouseCallback("Original pic", self.get_rgb)
        cv2.waitKey(0)
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '请选择图像  ')
        msg_box.exec_()

def get_rgb(self, event, x, y, a, b):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(self.img[y, x])
        self.ui.textBrowser_4.setText(' (%s, %s)' % (x, y))
        if self.c == 3:
            rgb = self.img[y, x]
            self.ui.textBrowser_3.setText(' R%s G%s B%s' % (rgb[2], rgb[1], rgb[0]))
        else:
            gray = self.img[y, x]
            self.ui.textBrowser_3.setText(' G %s ' % gray)

# 定义：图像显示到界面
def cvImgtoQtImg(cvImg,isConvertToGray=False):  # 定义opencv图像转PyQt图像的函数
    if isConvertToGray:
        QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
        QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_Grayscale8)
    else:
        QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGBA)
        QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_RGBA8888 )
    return QtImg

def image_HSV(self):
    if self.img.size > 1:
        img1 = self.img.copy()
        imgHSV = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
        self.img_save = imgHSV
        QtImg = cvImgtoQtImg(imgHSV)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_11.width(), self.ui.label_11.height())  # 设置图片大小
        self.ui.label_11.setPixmap(jpg_out_gray)  # 设置图片显示
    else:
        msg_box = QMessageBox(QMessageBox.Warning, '提示', '请选择图像  ')
        msg_box.exec_()









