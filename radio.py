# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Radio.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pexpect
import image_rc
from clock import DigitalClock

class Ui_gui(object):
    playing = False
    proc = pexpect.spawn('gst-play-1.0 1.mp3 2.mp3 3.mp3 4.mp3')
    
	
    def setupUi(self, gui):
        self.proc.send(' ')#
        gui.setObjectName("gui")
        gui.resize(654, 480)
        gui.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.Radio = QtWidgets.QTabWidget(gui)
        self.Radio.setGeometry(QtCore.QRect(0, 0, 640, 480))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Radio.setFont(font)
        self.Radio.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.Radio.setObjectName("Radio")
        self.home = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.home.setFont(font)
        self.home.setObjectName("home")
        ######
        #self.clock = QtWidgets.QTimeEdit(self.home)
        #self.clock.setGeometry(QtCore.QRect(60, 50, 531, 291))
        self.clock = DigitalClock(self.home)
        self.clock.setGeometry(QtCore.QRect(60, 50, 500, 300))
        self.clock.show()
        ######
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.clock.setFont(font)
        self.clock.setObjectName("clock")
        self.Radio.addTab(self.home, "")
        self.mp3 = QtWidgets.QWidget()
        self.mp3.setObjectName("mp3")
        self.volumeMp3 = QtWidgets.QSlider(self.mp3)
        self.volumeMp3.setGeometry(QtCore.QRect(20, 10, 81, 381))
        self.volumeMp3.setOrientation(QtCore.Qt.Vertical)
        self.volumeMp3.setObjectName("volumeMp3")
        self.playButton = QtWidgets.QPushButton(self.mp3)
        self.playButton.setGeometry(QtCore.QRect(320, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-image: url(:/images/play-button.png);\n"
"image: url(:/images/play-button.png);")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.muteButton = QtWidgets.QPushButton(self.mp3)
        self.muteButton.setGeometry(QtCore.QRect(460, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.muteButton.setFont(font)
        self.muteButton.setStyleSheet("background-image: url(:/images/mute.png);\n"
"image: url(:/images/mute.png);")
        self.muteButton.setText("")
        self.muteButton.setObjectName("muteButton")
        self.previousButton = QtWidgets.QPushButton(self.mp3)
        self.previousButton.setGeometry(QtCore.QRect(250, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet("background-image: url(:/images/previous.png);\n"
"image: url(:/images/previous.png);")
        self.previousButton.setText("")
        self.previousButton.setObjectName("previousButton")
        self.soundButton = QtWidgets.QPushButton(self.mp3)
        self.soundButton.setGeometry(QtCore.QRect(530, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.soundButton.setFont(font)
        self.soundButton.setStyleSheet("background-image: url(:/images/volume.png);\n"
"image: url(:/images/volume.png);")
        self.soundButton.setText("")
        self.soundButton.setObjectName("soundButton")
        self.nextButton = QtWidgets.QPushButton(self.mp3)
        self.nextButton.setGeometry(QtCore.QRect(390, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("background-image: url(:/images/next.png);\n"
"image: url(:/images/next.png);")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.pauseButton = QtWidgets.QPushButton(self.mp3)
        self.pauseButton.setGeometry(QtCore.QRect(180, 290, 61, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pauseButton.setFont(font)
        self.pauseButton.setStyleSheet("background-image: url(:/images/pause.png);\n"
"image: url(:/images/pause.png);")
        self.pauseButton.setText("")
        self.pauseButton.setObjectName("pauseButton")
        self.stopButton = QtWidgets.QPushButton(self.mp3)
        self.stopButton.setGeometry(QtCore.QRect(110, 290, 61, 61))
        self.stopButton.setStyleSheet("image: url(:/images/stop.png);\n"
"background-image: url(:/images/stop.png);")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.Radio.addTab(self.mp3, "")
        self.radio = QtWidgets.QWidget()
        self.radio.setObjectName("radio")
        self.lcdNumber = QtWidgets.QLCDNumber(self.radio)
        self.lcdNumber.setGeometry(QtCore.QRect(210, 0, 321, 121))
        self.lcdNumber.setObjectName("lcdNumber")
        self.dial = QtWidgets.QDial(self.radio)
        self.dial.setGeometry(QtCore.QRect(300, 170, 231, 231))
        self.dial.setObjectName("dial")
        self.verticalSlider = QtWidgets.QSlider(self.radio)
        self.verticalSlider.setGeometry(QtCore.QRect(30, 10, 91, 391))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.Radio.addTab(self.radio, "")

        self.retranslateUi(gui)
        self.Radio.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(gui)
        
        ################################################################
        ################################################################
        self.playButton.clicked.connect(self.play)
        self.stopButton.clicked.connect(self.stop)
        self.pauseButton.clicked.connect(self.pause)
        #self.soundButton.clicked.connect(self.sound)
        self.nextButton.clicked.connect(self.next)
        self.previousButton.clicked.connect(self.previous)
        #self.muteButton.clicked.connect(self.mute)
        #self.home. clicked.connect(self.homeClick)
        ################################################################
        ################################################################
        

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "Radio"))
        self.Radio.setTabText(self.Radio.indexOf(self.home), _translate("gui", "Home"))
        self.Radio.setTabText(self.Radio.indexOf(self.mp3), _translate("gui", "MP3"))
        self.Radio.setTabText(self.Radio.indexOf(self.radio), _translate("gui", "Radio"))

    def next(self, gui):
        self.proc.send('n')
        
    def previous(self, gui):
        self.proc.send('b')

    def pause(self, gui):
        self.proc.send(' ')
        
    def play(self, gui):
        self.proc.send(' ')
        
    def stop(self, gui):
        self.proc.send(' ')
        
    def homeClick(self, gui):
        self.proc.send(' ')
     
        
