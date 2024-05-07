global img
global point1, point2
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import time
from paddleocr import PaddleOCR, draw_ocr
import cv2
from PyQt5 import QtCore, QtGui,QtWidgets
ocr = PaddleOCR(use_angle_cls=True,use_gpu=False)
global result
global frame
from PIL import Image, ImageDraw, ImageFont

def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    if (isinstance(img, np.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def init(self):
    self.c2 = 1

# 关闭摄像头
def close_camera(self):
        self.camera_timer.stop()  # 停止读取
        self.cap.release()        # 释放摄像头
        self.camera_timer1.stop()  # 停止读取
        self.cap1.release()        # 释放摄像头
        self.ui.label_22.clear()     # 清除label组件上的图片
        self.ui.label_26.clear()     # 清除label组件上的图片

# 开启摄像头
def open_camera(self):
        self.chose = 2
        self.cap = cv2.VideoCapture(0)    # 摄像头
        if self.cap.isOpened():
            # 设置刷新参数
            a = self.ui.lineEdit_62.text()
            if len(str(a)) > 0:
                a = int(a)
                self.camera_timer.start(a)  # 每40毫秒读取一次，即刷新率为25帧
                self.show_image()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入参数')
                msg_box.exec_()
        else:
            QMessageBox.critical(self, '错误', '摄像头未打开！')
            return None

# 显示图片
def show_image(self):
        flag, image = self.cap.read()  # 从视频流中读取图片
        if(image is None):
            self.camera_timer.stop()  # 停止读取
            self.cap.release()   # 释放摄像头
            print("exit")
            return
        image_show = image
        QtImg = cvImgtoQtImg(image_show)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_22.width(), self.ui.label_22.height())  # 设置图片大小
        self.ui.label_22.setPixmap(jpg_out_gray)  # 设置图片显示

# 批量采集图像
def batch_collection_image(self):
        self.chose = 2
        self.cap1 = cv2.VideoCapture(0)    # 摄像头
        if self.cap1.isOpened():
            # 设置刷新参数
            a = self.ui.lineEdit_62.text()
            if len(str(a)) > 0:
                a = int(a)
                self.camera_timer1.start(a)  # 每40毫秒读取一次，即刷新率为25帧
                self.batch_show_image()
            else:
                msg_box = QMessageBox(QMessageBox.Warning, '提示', '请输入参数')
                msg_box.exec_()
        else:
            QMessageBox.critical(self, '错误', '摄像头未打开！')
            return None

def batch_show_image(self):
        now = time.localtime()
        flag1, image1 = self.cap1.read()  # 从视频流中读取图片
        if(image1 is None):
            self.camera_timer1.stop() # 停止读取
            self.cap1.release() #  释放摄像头
            print("exit")
            return
        image_show = image1
        QtImg = cvImgtoQtImg(image_show)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_22.width(), self.ui.label_22.height())  # 设置图片大小
        self.ui.label_22.setPixmap(jpg_out_gray)  # 设置图片显示

        nowt = time.strftime("%Y-%m-%d-%H_%M_%S", now)  # 这一步就是对时间进行格式化
        save_path = "Image_acquisition/batch_save_images/" + str(nowt) + ".jpg"
        save_img1 = str(nowt) + ".jpg"
        self.ui.textEdit_2.append("批量采集：" + save_img1)
        cv2.imwrite(save_path, image_show)

        image_show = cv2AddChineseText(image_show, "图像采集中", (20, 200), (0, 255, 0), 20)
        QtImg = cvImgtoQtImg(image_show)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_26.width(), self.ui.label_26.height())  # 设置图片大小
        self.ui.label_26.setPixmap(jpg_out_gray)  # 设置图片显示

# 单个采集图像
def single_collection_image(self):

    now = time.localtime()
    flag,image = self.cap.read()  # 从视频流中读取图片
    image_show = image

    nowt = time.strftime("%Y-%m-%d-%H_%M_%S", now)  # 这一步就是对时间进行格式化
    save_path = "Image_acquisition/single_save_image/" + str(nowt) + ".jpg"
    save_img = str(nowt) + ".jpg"
    self.ui.textEdit_2.append("单个采集：" + save_img)
    print(save_path)
    cv2.imwrite(save_path, image_show)
    image_show = cv2AddChineseText(image_show, "图像采集中", (20, 200), (0, 255, 0), 20)
    QtImg = cvImgtoQtImg(image_show)
    jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_26.width(), self.ui.label_26.height())  # 设置图片大小
    self.ui.label_26.setPixmap(jpg_out_gray)  # 设置图片显示

# =====================================================================================
# 打开图像
def choose_file_open(self):
        # 批量打开
        self.fileName_open = QFileDialog.getExistingDirectory(self, "选择源文件夹",".")
        self.ui.lineEdit_17.setText(self.fileName_open)

# 保存图像
def choose_file_save(self):
        # 批量打开
        self.fileName_save = QFileDialog.getExistingDirectory(self, "选择保存文件夹",".")
        self.ui.lineEdit_18.setText(self.fileName_save)


# 清空数据
def clear_all_2(self):
    self.img = np.ndarray(())
    self.imgOrg = np.ndarray(())
    self.imgShow = np.ndarray(())
    self.w = 0
    self.h = 0
    self.c = 1
    # 路径
    self.ui.lineEdit_18.setText('')
    self.ui.lineEdit_17.setText('')
    self.ui.lineEdit_10.setText('')
    self.ui.lineEdit_15.setText('')
    self.ui.lineEdit_16.setText('')

    self.ui.lineEdit_59.setText('')
    self.ui.lineEdit_56.setText('')
    self.ui.lineEdit_61.setText('')
    self.ui.lineEdit_58.setText('')
    self.ui.lineEdit_57.setText('')
    self.ui.lineEdit_60.setText('')
    # 数据显示框
    self.ui.textEdit_2.setText('')
    self.ui.label_22.setPixmap(QtGui.QPixmap(""))
    self.ui.label_26.setPixmap(QtGui.QPixmap(""))

def get_rgb_2(self, event, x, y, a, b):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(self.img[y, x])
        self.ui.textBrowser_5.setText(' (%s, %s)' % (x, y))
        if self.c == 3:
            rgb = self.img[y, x]
            self.ui.textBrowser_6.setText(' R%s G%s B%s' % (rgb[2], rgb[1], rgb[0]))
        else:
            gray = self.img[y, x]
            self.ui.textBrowser_6.setText(' G %s ' % gray)

# 定义：图像显示到界面
def cvImgtoQtImg(cvImg,isConvertToGray=False):  # 定义opencv图像转PyQt图像的函数
    if isConvertToGray:
        QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
        QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_Grayscale8)
    else:
        QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGBA)
        QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_RGBA8888 )
    return QtImg

def mousePressEvent(self, e):
    globalpos = e.globalPos()
    pos = self.ui.label_22.mapFromGlobal(globalpos)
    if pos.y() < 298 and pos.y() > 0 and pos.x() > 0 and pos.x() < 252:
        e.accept()

def mouseMoveEvent(self, e):
    globalpos = e.globalPos()
    pos = self.ui.label_22.mapFromGlobal(globalpos)
    if pos.y() < 298 and pos.y() > 0 and pos.x() > 0 and pos.x() < 252:
        h = self.img2Show.shape[0]
        w = self.img2Show.shape[1]
        e.accept()

