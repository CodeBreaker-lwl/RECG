# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Image_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1283, 664)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1281, 720))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 331, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_35.setGeometry(QtCore.QRect(200, 140, 91, 31))
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_41 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_41.setGeometry(QtCore.QRect(200, 80, 91, 31))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_42.setGeometry(QtCore.QRect(30, 140, 91, 31))
        self.pushButton_42.setObjectName("pushButton_42")
        self.lineEdit_62 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_62.setGeometry(QtCore.QRect(200, 30, 91, 31))
        self.lineEdit_62.setObjectName("lineEdit_62")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.label.setObjectName("label")
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_36.setGeometry(QtCore.QRect(30, 80, 91, 31))
        self.pushButton_36.setObjectName("pushButton_36")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_13.setGeometry(QtCore.QRect(350, 10, 911, 531))
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_26 = QtWidgets.QLabel(self.groupBox_13)
        self.label_26.setEnabled(True)
        self.label_26.setGeometry(QtCore.QRect(460, 20, 431, 501))
        self.label_26.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_26.setMouseTracking(False)
        self.label_26.setAutoFillBackground(True)
        self.label_26.setFrameShape(QtWidgets.QFrame.Box)
        self.label_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.label_22 = QtWidgets.QLabel(self.groupBox_13)
        self.label_22.setEnabled(True)
        self.label_22.setGeometry(QtCore.QRect(20, 20, 421, 501))
        self.label_22.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_22.setMouseTracking(False)
        self.label_22.setAutoFillBackground(True)
        self.label_22.setFrameShape(QtWidgets.QFrame.Box)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 220, 331, 321))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 20, 311, 291))
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 310, 341, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(120, 100, 51, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 60, 91, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 91, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 60, 91, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 20, 91, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_34.setGeometry(QtCore.QRect(220, 100, 91, 28))
        self.pushButton_34.setObjectName("pushButton_34")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 100, 81, 31))
        self.label_12.setObjectName("label_12")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setEnabled(True)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 341, 291))
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_10.setMouseTracking(False)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setFrameShape(QtWidgets.QFrame.Box)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(370, 10, 891, 401))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_11.setMouseTracking(False)
        self.label_11.setAutoFillBackground(True)
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 460, 341, 121))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser_4.setGeometry(QtCore.QRect(70, 60, 251, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(70, 20, 251, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(20, 70, 31, 31))
        self.label_15.setObjectName("label_15")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 31, 21))
        self.label_7.setObjectName("label_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 420, 891, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 871, 131))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 330, 391, 251))
        self.groupBox_6.setObjectName("groupBox_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 140, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_30.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_37 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_37.setGeometry(QtCore.QRect(20, 140, 101, 31))
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_32.setGeometry(QtCore.QRect(20, 80, 101, 31))
        self.pushButton_32.setObjectName("pushButton_32")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(130, 140, 81, 31))
        self.label_13.setObjectName("label_13")
        self.pushButton_79 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_79.setGeometry(QtCore.QRect(20, 200, 101, 31))
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_80.setGeometry(QtCore.QRect(270, 200, 101, 31))
        self.pushButton_80.setObjectName("pushButton_80")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 20, 251, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 80, 251, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_7.setGeometry(QtCore.QRect(810, 420, 451, 161))
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit_5 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 20, 431, 131))
        self.textEdit_5.setObjectName("textEdit_5")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_9)
        self.groupBox_8.setGeometry(QtCore.QRect(410, 420, 381, 161))
        self.groupBox_8.setObjectName("groupBox_8")
        self.textEdit_6 = QtWidgets.QTextEdit(self.groupBox_8)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 20, 361, 131))
        self.textEdit_6.setObjectName("textEdit_6")
        self.label_2 = QtWidgets.QLabel(self.tab_9)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 391, 311))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab_9)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 841, 401))
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_3)
        self.listWidget_2.setGeometry(QtCore.QRect(40, 90, 581, 491))
        self.listWidget_2.setStyleSheet("border-width: 1px;\n"
"border-style: solid;\n"
"")
        self.listWidget_2.setObjectName("listWidget_2")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_9.setGeometry(QtCore.QRect(40, 10, 581, 71))
        self.groupBox_9.setObjectName("groupBox_9")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_33.setGeometry(QtCore.QRect(460, 20, 101, 31))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_38 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_38.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.pushButton_38.setObjectName("pushButton_38")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.groupBox_9)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(190, 20, 211, 31))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(720, 10, 531, 71))
        self.groupBox_10.setObjectName("groupBox_10")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_20.setGeometry(QtCore.QRect(30, 20, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_10)
        self.pushButton_21.setGeometry(QtCore.QRect(410, 20, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.pushButton_21.setMinimumSize(QtCore.QSize(99, 0))
        self.pushButton_21.setObjectName("pushButton_21")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(720, 90, 531, 491))
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1283, 23))
        self.menubar.setObjectName("menubar")
        self.menuun1 = QtWidgets.QMenu(self.menubar)
        self.menuun1.setObjectName("menuun1")
        self.menucx = QtWidgets.QMenu(self.menubar)
        self.menucx.setObjectName("menucx")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuun1.menuAction())
        self.menubar.addAction(self.menucx.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "操作区"))
        self.pushButton_35.setText(_translate("MainWindow", "批量采集"))
        self.pushButton_41.setText(_translate("MainWindow", "关闭摄像头"))
        self.pushButton_42.setText(_translate("MainWindow", "单个采集"))
        self.lineEdit_62.setText(_translate("MainWindow", "100"))
        self.label.setText(_translate("MainWindow", "视频帧数设置："))
        self.pushButton_36.setText(_translate("MainWindow", "打开摄像头"))
        self.groupBox_13.setTitle(_translate("MainWindow", "图像显示"))
        self.groupBox_5.setTitle(_translate("MainWindow", "采集图像信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "图像采集"))
        self.groupBox_3.setTitle(_translate("MainWindow", "操作区"))
        self.lineEdit.setText(_translate("MainWindow", "300"))
        self.pushButton_3.setText(_translate("MainWindow", "保存图像"))
        self.pushButton.setText(_translate("MainWindow", "选择图像"))
        self.pushButton_4.setText(_translate("MainWindow", "清空图像"))
        self.pushButton_2.setText(_translate("MainWindow", "重置图像"))
        self.pushButton_34.setText(_translate("MainWindow", "图像识别"))
        self.label_12.setText(_translate("MainWindow", "判定参数设置："))
        self.groupBox.setTitle(_translate("MainWindow", "图像信息"))
        self.label_15.setText(_translate("MainWindow", "定位"))
        self.label_7.setText(_translate("MainWindow", "大小"))
        self.groupBox_2.setTitle(_translate("MainWindow", "识别结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "图像识别"))
        self.groupBox_6.setTitle(_translate("MainWindow", "操作区"))
        self.lineEdit_2.setText(_translate("MainWindow", "300"))
        self.pushButton_30.setText(_translate("MainWindow", "批量打开"))
        self.pushButton_37.setText(_translate("MainWindow", "图像识别"))
        self.pushButton_32.setText(_translate("MainWindow", "批量保存"))
        self.label_13.setText(_translate("MainWindow", "判定参数设置："))
        self.pushButton_79.setText(_translate("MainWindow", "清空图像"))
        self.pushButton_80.setText(_translate("MainWindow", "清空数据"))
        self.groupBox_7.setTitle(_translate("MainWindow", "识别结果"))
        self.groupBox_8.setTitle(_translate("MainWindow", "处理过程"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "批量识别"))
        self.groupBox_9.setTitle(_translate("MainWindow", "识别图像查看"))
        self.pushButton_33.setText(_translate("MainWindow", "清空图像"))
        self.pushButton_38.setText(_translate("MainWindow", "打开图像文件"))
        self.groupBox_10.setTitle(_translate("MainWindow", "识别结果查看"))
        self.pushButton_20.setText(_translate("MainWindow", "打开数据文件"))
        self.pushButton_21.setText(_translate("MainWindow", "关闭"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "结果查看"))
        self.menuun1.setTitle(_translate("MainWindow", "开始"))
        self.menucx.setTitle(_translate("MainWindow", "编辑"))
        self.menu.setTitle(_translate("MainWindow", "帮助"))
        self.menu_2.setTitle(_translate("MainWindow", "关于"))

