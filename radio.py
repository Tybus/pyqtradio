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
    currentStation = 88.8
    proc = pexpect.spawn('gst-play-1.0 1.mp3 2.mp3 3.mp3 4.mp3')
    def setupUi(self, gui):
        self.proc.send(' ')#
        gui.setObjectName("gui")
        gui.resize(640, 480)
        gui.setStyleSheet("background-color: rgb(32, 74, 135);")
        self.gridLayout = QtWidgets.QGridLayout(gui)
        self.gridLayout.setObjectName("gridLayout")
        self.Radio = QtWidgets.QTabWidget(gui)
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
        self.clock.setObjectName("clock")
        self.Radio.addTab(self.home, "")
        self.mp3 = QtWidgets.QWidget()
        self.mp3.setObjectName("mp3")
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
        self.stationDisplay = QtWidgets.QLCDNumber(self.radio)
        self.stationDisplay.setGeometry(QtCore.QRect(140, 40, 261, 131))
        self.stationDisplay.setSmallDecimalPoint(True)
        self.stationDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.stationDisplay.setProperty("value", self.currentStation)############################
        self.stationDisplay.setObjectName("stationDisplay")
        self.previousStation = QtWidgets.QPushButton(self.radio)
        self.previousStation.setGeometry(QtCore.QRect(180, 200, 71, 81))
        self.previousStation.setStyleSheet("background-image: url(:/images/previous.png);\n"
"image: url(:/images/previous.png);")
        self.previousStation.setText("")
        self.previousStation.setObjectName("previousStation")
        self.nextStation = QtWidgets.QPushButton(self.radio)
        self.nextStation.setGeometry(QtCore.QRect(340, 200, 71, 81))
        self.nextStation.setStyleSheet("background-image: url(:/images/next.png);\n"
"image: url(:/images/next.png);")
        self.nextStation.setText("")
        self.nextStation.setObjectName("nextStation")
        self.playRadio = QtWidgets.QPushButton(self.radio)
        self.playRadio.setGeometry(QtCore.QRect(260, 200, 71, 81))
        self.playRadio.setStyleSheet("background-image: url(:/images/play-button.png);\n"
"image: url(:/images/play-button.png);")
        self.playRadio.setText("")
        self.playRadio.setObjectName("playRadio")
        self.textBrowser = QtWidgets.QTextBrowser(self.radio)
        self.textBrowser.setGeometry(QtCore.QRect(410, 130, 81, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.Radio.addTab(self.radio, "")
        self.gridLayout.addWidget(self.Radio, 0, 0, 1, 1)
        self.actionabc = QtWidgets.QAction(gui)
        self.actionabc.setObjectName("actionabc")

        self.retranslateUi(gui)
        self.Radio.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gui)

        ################################################################
        self.playButton.clicked.connect(self.play)
        self.stopButton.clicked.connect(self.stop)
        self.pauseButton.clicked.connect(self.pause)
        #self.soundButton.clicked.connect(self.sound)
        self.nextButton.clicked.connect(self.next)
        self.previousButton.clicked.connect(self.previous)
        #self.muteButton.clicked.connect(self.mute)
        #self.home. clicked.connect(self.homeClick)
        self.playRadio.clicked.connect(self.stopMP3)
        self.nextStation.clicked.connect(self.passNextStation)
        self.previousStation.clicked.connect(self.passPreviousStation)
        ################################################################

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "Radio"))
        self.Radio.setTabText(self.Radio.indexOf(self.home), _translate("gui", "Home"))
        self.Radio.setTabText(self.Radio.indexOf(self.mp3), _translate("gui", "MP3"))
        self.textBrowser.setHtml(_translate("gui", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">MHz</span></p></body></html>"))
        self.Radio.setTabText(self.Radio.indexOf(self.radio), _translate("gui", "Radio"))
        self.actionabc.setText(_translate("gui", "abc"))

    def next(self, gui):
        self.proc.send('n')
        
    def previous(self, gui):
        self.proc.send('b')

    def pause(self, gui):
        self.proc.send(' ')
        
    def play(self, gui):
        self.playing = True
        self.proc.send(' ')
        
    def stopMP3(self, gui):
        if self.playing == True:
            self.proc.send(' ')
            self.playing = False
        
    def stop(self, gui):
        self.proc.send(' ')
        
    def homeClick(self, gui):
        self.proc.send(' ')
    
    def passNextStation(self, gui):
        self.currentStation+=0.1
        self.stationDisplay.setProperty("value", self.currentStation)
    def passPreviousStation(self, gui):
        self.currentStation-=0.1
        self.stationDisplay.setProperty("value", self.currentStation)
