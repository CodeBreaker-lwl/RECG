import Image_ui as Image_ui
import page1, page2, page3, page4
from PyQt5.QtCore import QTimer
import sys
import numpy as np
from PyQt5.QtCore import QSize
import PyQt5_stylesheets
from denglu import Ui_Dialog5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import *

"显示多张图片的缩略图 加滚动条"
FrameIdxRole = Qt.UserRole + 1


class MainDialog(QMainWindow):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.ui = Image_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("文字识别系统")
        self.m_drag = False
        self.img = np.ndarray(())
        self.imgOrg = np.ndarray(())
        self.imgShow = np.ndarray(())
        self.mask = np.ndarray(())
        self.img_segmentation = np.ndarray(())
        self.img_segmentation2 = np.ndarray(())
        self.img_segmentation4 = np.ndarray(())
        self.img_large = np.ndarray(())
        self.img_color_un = np.ndarray(())
        self.img_color_un_5 = np.ndarray(())
        self.img_save = np.ndarray(())
        self.img_save1 = np.ndarray(())
        self.point = []
        self.fname = ''
        self.file_name = ''
        self.kernel = ''
        self.kernel1 = ''
        self.threshold_value = 0
        self.w = 0
        self.h = 0
        self.c = 1
        self.chose = 0
        self.determine = 0
        self.fileName_save = ''
        # ==================page1: 图像识别=========================
        self.ui.pushButton.clicked.connect(self.select_button_clicked)  # 打开图像
        self.ui.pushButton_2.clicked.connect(self.reset)  # 重置图像
        self.ui.pushButton_3.clicked.connect(self.saveimg)  # 保存图像
        self.ui.pushButton_4.clicked.connect(self.clear)  # 清除图像
        self.ui.pushButton_34.clicked.connect(self.image_recognition)  # 图像识别

        # ==================page2：图像采集=========================
        page2.init(self)
        self.camera_timer = QTimer()
        self.camera_timer.timeout.connect(self.show_image)
        self.camera_timer1 = QTimer()
        self.camera_timer1.timeout.connect(self.batch_show_image)
        self.ui.pushButton_36.clicked.connect(self.open_camera)  # 选择图像文件夹
        self.ui.pushButton_35.clicked.connect(self.batch_collection_image)  # 批量采集
        self.ui.pushButton_41.clicked.connect(self.close_camera)
        self.ui.pushButton_42.clicked.connect(self.single_collection_image)  # 单个采集

        # ==================page3: 批量图像识别=========================
        page3.init(self)
        self.ui.pushButton_30.clicked.connect(self.choose_file_open)  # 批量打开图像
        self.ui.pushButton_32.clicked.connect(self.choose_file_save)  # 批量保存图像
        self.ui.pushButton_37.clicked.connect(self.batch_image_recognition)  # 批量识别图像
        self.ui.pushButton_79.clicked.connect(self.clear_img_3)  # 清空图像
        self.ui.pushButton_80.clicked.connect(self.clear_data_3)  # 清空图像

        # ==================page4：识别结果查看====================================
        page4.init(self)
        self.ui.pushButton_38.clicked.connect(self.choose_file_4)
        self.ui.pushButton_33.clicked.connect(self.clear_img_4)
        self.ui.pushButton_20.clicked.connect(self.openfile_5)  # 清空图像
        self.ui.pushButton_21.clicked.connect(self.onButtonClick)

    # ========================== page3======================
    def clear_img_3(self):
        return page3.clear_img_3(self)

    def clear_data_3(self):
        return page3.clear_data_3(self)

    def choose_file_open(self):
        return page3.choose_file_open(self)

    def choose_file_save(self):
        return page3.choose_file_save(self)

    def batch_image_recognition(self):
        return page3.batch_image_recognition(self)

    # ========================== page4======================
    def openfile_5(self):
        return page4.openfile_5(self)

    def choose_file_4(self):
        return page4.choose_file_4(self)

    def clear_img_4(self):
        return page4.clear_img_4(self)

    def add_image_thumbnail(self, image, frameIdx, name):
        self.ui.listWidget_2.itemSelectionChanged.disconnect(self.onItemSelectionChanged)
        height, width, channels = image.shape
        # print(image.shape)
        bytes_per_line = width * channels
        # print(bytes_per_line)
        qImage = QImage(image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(qImage)

        item = QListWidgetItem(QIcon(pixmap), str(frameIdx) + ": " + name)
        # ------------------------------------
        item.setData(FrameIdxRole, frameIdx)
        self.ui.listWidget_2.addItem(item)
        self.ui.listWidget_2.setCurrentRow(self.ui.listWidget_2.count() - 1)  # 列表小部件计数
        self.ui.listWidget_2.itemSelectionChanged.connect(self.onItemSelectionChanged)

    def onItemSelectionChanged(self):
        pass

    def onSliderPosChanged_9(self, value):
        self.ui.listWidget_2.setIconSize(QSize(value, value))

    def openfile_4(self):
        return page4.openfile_5(self)

    def showHead(self, head):
        return page4.showHead(self, head)

    def showRecord(self, line, lineNO):
        return page4.showRecord(self, line, lineNO)

    def creat_table_show_5(self):  # creat_table_show
        return page4.creat_table_show_5(self)

    def onButtonClick(self):
        # sender 是发送信号的对象，此处发送信号的对象是button1按钮
        sender = self.sender()
        print(sender.text() + ' 被按下了')
        qApp = QApplication.instance()
        qApp.quit()

    # ========================== page1======================
    def clear(self):
        return page1.clear(self)

    def image_recognition(self):
        return page1.image_recognition(self)

    def reset(self):
        return page1.reset(self)

    def saveimg(self):
        return page1.saveimg(self)

    def showlarge(self):
        return page1.showlarge(self)

    def get_rgb(self, event, x, y, a, b):
        return page1.get_rgb(self, event, x, y, a, b)

    def select_button_clicked(self):
        return page1.select_button_clicked(self)

    # ========================== page2======================
    #
    def clear_all_2(self):
        return page2.clear_all_2(self)

    def batch_show_image(self):
        return page2.batch_show_image(self)

    def show_image(self):
        return page2.show_image(self)

    def open_camera(self):
        return page2.open_camera(self)

    def close_camera(self):
        return page2.close_camera(self)

    def single_collection_image(self):
        return page2.single_collection_image(self)

    def batch_collection_image(self):
        return page2.batch_collection_image(self)

    def get_rgb_2(self, event, x, y, a, b):
        return page2.get_rgb_2(self, event, x, y, a, b)

    def mousePressEvent(self, e):
        if Qt.LeftButton:
            if self.ui.tabWidget.currentIndex() == 1:
                return page2.mousePressEvent(self, e)

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_drag:
            if self.ui.tabWidget.currentIndex() == 1:
                return page2.mousePressEvent(self, e)


USER_PWD = {
    'la_vie': 'password',
    '1':  # 账号
        '1'  # 密码
}


class LoginWindow(QDialog, Ui_Dialog5):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)  # #初始化界面内
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.pushButton.clicked.connect(self.go_to_inter)

    # 判断用户密码是否正确
    def go_to_inter(self):
        if USER_PWD.get(self.lineEdit.text()) != (self.lineEdit_2.text() and self.lineEdit_3.text()):
            QMessageBox.critical(self, 'Wrong', '用户名或密码错误!')
            return
        self.accept()
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_blue"))
    app.setWindowIcon(QIcon('./PyQt5_stylesheets/logo.ico'))
    dialog = LoginWindow()
    if dialog.exec_() == QDialog.Accepted:
        Dlg = MainDialog()
        Dlg.show()
    sys.exit(app.exec_())

python3: input("please input any key to exit!")
