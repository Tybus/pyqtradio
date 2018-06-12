# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Radio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import images_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer # Load the required library

class Ui_Radio(object):
    def setupUi(self, Radio):
        Radio.setObjectName("Radio")
        Radio.resize(640, 480)
        Radio.setStyleSheet("background-color: rgb(138, 149, 151);\n"
"border-color: rgb(138, 149, 151);")
        self.tabWidget = QtWidgets.QTabWidget(Radio)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 640, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(138, 149, 151);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.home)
        self.dateTimeEdit.setGeometry(QtCore.QRect(70, 50, 511, 321))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.tabWidget.addTab(self.home, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.FrecuencyDisplay = QtWidgets.QLCDNumber(self.tab)
        self.FrecuencyDisplay.setGeometry(QtCore.QRect(110, 40, 461, 191))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FrecuencyDisplay.sizePolicy().hasHeightForWidth())
        self.FrecuencyDisplay.setSizePolicy(sizePolicy)
        self.FrecuencyDisplay.setObjectName("FrecuencyDisplay")
        self.horizontalSlider = QtWidgets.QSlider(self.tab)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 360, 571, 61))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.volumeSliderRadio = QtWidgets.QSlider(self.tab)
        self.volumeSliderRadio.setGeometry(QtCore.QRect(20, 30, 61, 301))
        self.volumeSliderRadio.setOrientation(QtCore.Qt.Vertical)
        self.volumeSliderRadio.setObjectName("volumeSliderRadio")
        self.tabWidget.addTab(self.tab, "")
        self.mp3 = QtWidgets.QWidget()
        self.mp3.setObjectName("mp3")
        self.previousButton = QtWidgets.QPushButton(self.mp3)
        self.previousButton.setGeometry(QtCore.QRect(230, 220, 71, 71))
        font = QtGui.QFont()
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet("image: url(:/images/back.png);\n"
"background-image: url(:/images/blue.png);")
        self.previousButton.setText("")
        self.previousButton.setObjectName("previousButton")
        self.playButton = QtWidgets.QPushButton(self.mp3)
        self.playButton.setGeometry(QtCore.QRect(310, 220, 71, 71))
        font = QtGui.QFont()
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-image: url(:/images/blue.png);\n"
"image: url(:/images/play.png);\n"
"")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        ######################################################################
        self.playButton.clicked.connect(self.play)
        ######################################################################
        self.nextButton = QtWidgets.QPushButton(self.mp3)
        self.nextButton.setGeometry(QtCore.QRect(390, 220, 61, 71))
        font = QtGui.QFont()
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("background-image: url(:/images/blue.png);\n"
"image: url(:/images/forward.png);")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.volumSliderMP3 = QtWidgets.QSlider(self.mp3)
        self.volumSliderMP3.setGeometry(QtCore.QRect(15, 29, 71, 301))
        self.volumSliderMP3.setOrientation(QtCore.Qt.Vertical)
        self.volumSliderMP3.setObjectName("volumSliderMP3")
        self.textBrowser = QtWidgets.QTextBrowser(self.mp3)
        self.textBrowser.setGeometry(QtCore.QRect(120, 151, 451, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.mp3, "")

        self.retranslateUi(Radio)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Radio)

    def retranslateUi(self, Radio):
        _translate = QtCore.QCoreApplication.translate
        Radio.setWindowTitle(_translate("Radio", "Radio Incrustada"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home), _translate("Radio", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Radio", "Radio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mp3), _translate("Radio", "MP3"))

    def play(self, Radio):
        mixer.init()
        #mixer.music.load('/media/gab/9e5e7199-9d10-4f68-8f58-7381ad0c1c39/gab/Qt5Desings/test.mp3')
        mixer.music.load('test.mp3')
        mixer.music.play()
        #mixer.music.stop()

