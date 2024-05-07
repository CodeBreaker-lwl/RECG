# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denglu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog5(object):
    def setupUi(self, Dialog5):
        Dialog5.setObjectName("Dialog5")
        Dialog5.resize(1044, 697)
        self.centralwidget = QtWidgets.QWidget(Dialog5)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 90, 451, 471))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 541, 471))
        self.label_2.setStyleSheet("background-image: url(:/back/back/3.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(640, 100, 201, 61))
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(640, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border:none;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-bottom:2px solid rgba(0,0,0,100);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(640, 270, 251, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(0,0,0,100);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 450, 161, 61))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 190, 371, 81))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(640, 350, 251, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(15)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border:none;\n"
"border-bottom:2px solid rgba(0,0,0,100);\n"
"background-color: rgba(0, 0, 0, 0);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(880, 90, 128, 53))
        self.frame.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-botton:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/minisize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/maxsize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        # Dialog5.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dialog5)
        self.pushButton_3.clicked.connect(Dialog5.close)
        self.pushButton_4.clicked.connect(Dialog5.showMinimized)
        self.pushButton_2.clicked.connect(Dialog5.showMaximized)
        QtCore.QMetaObject.connectSlotsByName(Dialog5)

    def retranslateUi(self, Dialog5):
        _translate = QtCore.QCoreApplication.translate
        Dialog5.setWindowTitle(_translate("Dialog5", "MainWindow"))
        self.label_4.setText(_translate("Dialog5", "欢迎登录"))
        self.lineEdit.setPlaceholderText(_translate("Dialog5", "用户账号："))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog5", "密    码："))
        self.pushButton.setText(_translate("Dialog5", "登录"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog5", "确认密码："))

import bs_rc
