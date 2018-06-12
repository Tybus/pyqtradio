# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Radio.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pygame import mixer # Load the required library

class Ui_Radio(object):
    def setupUi(self, Radio):
        Radio.setObjectName("Radio")
        Radio.resize(640, 480)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Radio)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 89, 621, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayoutWidget = QtWidgets.QWidget(Radio)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 621, 78))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MP3Button = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.MP3Button.setObjectName("MP3Button")
        ######################################################################
        self.MP3Button.clicked.connect(self.play)
        ######################################################################
        self.gridLayout.addWidget(self.MP3Button, 1, 0, 1, 1)
        self.RadioButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.RadioButton.setObjectName("RadioButton")
        self.gridLayout.addWidget(self.RadioButton, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Radio)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 140, 21, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalLayout.addWidget(self.verticalSlider)

        self.retranslateUi(Radio)
        QtCore.QMetaObject.connectSlotsByName(Radio)

    def retranslateUi(self, Radio):
        _translate = QtCore.QCoreApplication.translate
        Radio.setWindowTitle(_translate("Radio", "Radio Incrustada"))
        self.MP3Button.setText(_translate("Radio", "MP3"))
        self.RadioButton.setText(_translate("Radio", "Radio"))

    def play(self, Radio):
        mixer.init()
        #mixer.music.load('/media/gab/9e5e7199-9d10-4f68-8f58-7381ad0c1c39/gab/Qt5Desings/test.mp3')
        mixer.music.load('test.mp3')
        mixer.music.play()
        #mixer.music.stop()



