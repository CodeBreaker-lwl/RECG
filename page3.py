global img
global point1, point2
from PyQt5.QtWidgets import *
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import threading
import os
from paddleocr import PaddleOCR, draw_ocr
import cv2
from PyQt5 import QtCore, QtGui,QtWidgets
ocr = PaddleOCR(use_angle_cls=True,use_gpu=False)
global result
global frame
from PIL import Image, ImageDraw, ImageFont
from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import time

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

def cvImgtoQtImg(cvImg,isConvertToGray=False):
        if isConvertToGray:
            QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2GRAY)
            QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_Grayscale8)
        else:
            QtImgBuf = cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGBA)
            QtImg = QtGui.QImage(QtImgBuf.data, QtImgBuf.shape[1], QtImgBuf.shape[0], QtGui.QImage.Format_RGBA8888 )
        return QtImg

def init(self):
    self.c2 = 1

# 批量打开图像
def choose_file_open(self):
        self.fileName_open = QFileDialog.getExistingDirectory(self, "选择源文件夹",".")
        self.ui.lineEdit_3.setText(self.fileName_open)

# 批量保存图像
def choose_file_save(self):
        self.fileName_save = QFileDialog.getExistingDirectory(self, "选择保存文件夹",".")
        self.ui.lineEdit_4.setText(self.fileName_save)

def batch_image_recognition_image(self,file_name):
    imgs = os.listdir(file_name)
    for img in imgs:
        # 实时刷新界面
        QApplication.processEvents()
        source_img = file_name + '/' + str(img)
        print("源文件夹路径",source_img)
        # 读取原图像与显示
        src = cv2.imread(source_img)
        QtImg = cvImgtoQtImg(src)
        jpg_src_bright = QtGui.QPixmap(QtImg).scaled(self.ui.label_2.width(), self.ui.label_2.height())  # 设置图片大小
        self.ui.label_2.setPixmap(jpg_src_bright)  # 设置图片显示

        now = time.localtime()
        ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
        img_path = source_img
        result = ocr.ocr(img_path, cls=True)
        for line in result:
            print(line)
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]

        nowt = time.strftime("%Y-%m-%d-%H_%M_%S", now)  # 这一步就是对时间进行格式化
        image_recognition_results = "number: " + str(txts) + "scores: " + str(scores)
        image_recognition_results1 = str(img) + "  " + str(txts) + "scores" + "  " + str(scores)
        # 保存到text
        with open('data_recognition_result_saving/save_data/batch_result.txt', 'a', encoding='utf-8') as f:
               f.write(image_recognition_results1 + '\n')

        self.ui.textEdit_5.append("识别结果："+nowt+image_recognition_results)
        im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/fonts/simfang.ttf')
        QtImg = cvImgtoQtImg(im_show)
        jpg_out_gray = QtGui.QPixmap(QtImg).scaled(self.ui.label_3.width(), self.ui.label_3.height())  # 设置图片大小
        self.ui.label_3.setPixmap(jpg_out_gray)  # 设置图片显示

        # 保存图像
        resize_save3 = self.fileName_save + '/' + str(img)
        print("保存文件夹路径",resize_save3)
        cv2.imwrite(resize_save3, im_show)
        self.ui.textEdit_6.append(" 正在处理图像：{}".format(source_img))

def batch_image_recognition(self):
    start_time1 = time.time()
    path = self.fileName_open
    # 循环执行次数
    t = threading.Thread(target=batch_image_recognition_image(self, path))
    t.start()  # 启动线程，即让线程开始执行
    end_time1 = time.time()
    print(end_time1 - start_time1)
    print("完成")

def clear_data_3(self):
    self.img = np.ndarray(())
    self.imgOrg = np.ndarray(())
    self.imgShow = np.ndarray(())
    self.w = 0
    self.h = 0
    self.c = 1
    # 路径
    self.ui.lineEdit_3.setText('')
    self.ui.lineEdit_4.setText('')
    self.ui.lineEdit_2.setText('')
    self.ui.textEdit_6.setText('')
    self.ui.textEdit_5.setText('')

# 清空数据
def clear_img_3(self):
    self.img = np.ndarray(())
    self.imgOrg = np.ndarray(())
    self.imgShow = np.ndarray(())
    self.w = 0
    self.h = 0
    self.c = 1
    self.ui.label_2.setPixmap(QtGui.QPixmap(""))
    self.ui.label_3.setPixmap(QtGui.QPixmap(""))

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

