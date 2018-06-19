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
import glob

class Ui_gui(object):
    playing = False
    #currentSong = 'EiE Theme'
    currentSongIndex = 0
    playListRoute = ''
    #playList = glob.glob(self.playListRoute+'*.mp3')
    #playListJoin = ' '.join(glob.glob(self.playListRoute+'*.mp3'))#glob.glob('/home/gab/Qt5/RadioGUI/pyqtradio-master/*.mp3')  
    #playListLengh = len(playList)
    currentStation = 88.8
    #proc = pexpect.spawn('gst-play-1.0 '+ playListJoin)
    
    def __init__(self, playListRoute):
        self.playListRoute = playListRoute
        self.playList = glob.glob(playListRoute+'*.mp3')
        self.playListJoin = ' '.join(glob.glob(playListRoute+'*.mp3'))
        self.proc = pexpect.spawn('gst-play-1.0 '+ self.playListJoin)
        self.playListLengh = len(self.playList)
        print(self.playListRoute)
    
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_3.setObjectName("gridLayout_3")
        ######
        #self.clock = QtWidgets.QTimeEdit(self.home)
        #self.clock.setGeometry(QtCore.QRect(60, 50, 531, 291))
        self.clock = DigitalClock(self.home)
        self.clock.setGeometry(QtCore.QRect(60, 50, 500, 300))
        self.clock.show()
        ######
        self.gridLayout_3.addWidget(self.clock, 0, 0, 1, 1)
        self.Radio.addTab(self.home, "")
        self.mp3 = QtWidgets.QWidget()
        self.mp3.setObjectName("mp3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mp3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stopButton = QtWidgets.QPushButton(self.mp3)
        self.stopButton.setStyleSheet("image: url(:/images/stop.png);\n"
"background-image: url(:/images/stop.png);")
        self.stopButton.setText("")
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 0, 0, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(self.mp3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pauseButton.setFont(font)
        self.pauseButton.setStyleSheet("background-image: url(:/images/pause.png);\n"
"image: url(:/images/pause.png);")
        self.pauseButton.setText("")
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout_2.addWidget(self.pauseButton, 0, 1, 1, 1)
        self.previousButton = QtWidgets.QPushButton(self.mp3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.previousButton.setFont(font)
        self.previousButton.setStyleSheet("background-image: url(:/images/previous.png);\n"
"image: url(:/images/previous.png);")
        self.previousButton.setText("")
        self.previousButton.setObjectName("previousButton")
        self.gridLayout_2.addWidget(self.previousButton, 0, 2, 1, 1)
        self.playButton = QtWidgets.QPushButton(self.mp3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.playButton.setFont(font)
        self.playButton.setStyleSheet("background-image: url(:/images/play-button.png);\n"
"image: url(:/images/play-button.png);")
        self.playButton.setText("")
        self.playButton.setObjectName("playButton")
        self.gridLayout_2.addWidget(self.playButton, 0, 3, 1, 1)
        self.nextButton = QtWidgets.QPushButton(self.mp3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet("background-image: url(:/images/next.png);\n"
"image: url(:/images/next.png);")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.gridLayout_2.addWidget(self.nextButton, 0, 4, 1, 1)
        self.muteButton = QtWidgets.QPushButton(self.mp3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.muteButton.setFont(font)
        self.muteButton.setStyleSheet("background-image: url(:/images/mute.png);\n"
"image: url(:/images/mute.png);")
        self.muteButton.setText("")
        self.muteButton.setObjectName("muteButton")
        self.gridLayout_2.addWidget(self.muteButton, 0, 5, 1, 1)
        self.soundButton = QtWidgets.QPushButton(self.mp3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.soundButton.setFont(font)
        self.soundButton.setStyleSheet("background-image: url(:/images/volume.png);\n"
"image: url(:/images/volume.png);")
        self.soundButton.setText("")
        self.soundButton.setObjectName("soundButton")
        self.gridLayout_2.addWidget(self.soundButton, 0, 6, 1, 1)
        self.Radio.addTab(self.mp3, "")
        self.radio = QtWidgets.QWidget()
        self.radio.setObjectName("radio")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.radio)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.previousStation = QtWidgets.QPushButton(self.radio)
        self.previousStation.setStyleSheet("background-image: url(:/images/previous.png);\n"
"image: url(:/images/previous.png);")
        self.previousStation.setText("")
        self.previousStation.setObjectName("previousStation")
        self.gridLayout_4.addWidget(self.previousStation, 1, 0, 1, 1)
        self.nextStation = QtWidgets.QPushButton(self.radio)
        self.nextStation.setStyleSheet("background-image: url(:/images/next.png);\n"
"image: url(:/images/next.png);")
        self.nextStation.setText("")
        self.nextStation.setObjectName("nextStation")
        self.gridLayout_4.addWidget(self.nextStation, 1, 2, 1, 1)
        self.playRadio = QtWidgets.QPushButton(self.radio)
        self.playRadio.setStyleSheet("background-image: url(:/images/play-button.png);\n"
"image: url(:/images/play-button.png);")
        self.playRadio.setText("")
        self.playRadio.setObjectName("playRadio")
        self.gridLayout_4.addWidget(self.playRadio, 1, 1, 1, 1)
        self.stationDisplay = QtWidgets.QLCDNumber(self.radio)
        self.stationDisplay.setSmallDecimalPoint(True)
        self.stationDisplay.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.stationDisplay.setProperty("value", 88.8)
        self.stationDisplay.setObjectName("stationDisplay")
        self.gridLayout_4.addWidget(self.stationDisplay, 0, 0, 1, 3)
        self.Radio.addTab(self.radio, "")
        self.gridLayout.addWidget(self.Radio, 0, 0, 1, 1)
        self.actionabc = QtWidgets.QAction(gui)
        self.actionabc.setObjectName("actionabc")

        self.retranslateUi(gui)
        self.Radio.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gui)
        
        self.stationDisplay.setProperty("value", self.currentStation)############################
        ################################################################
        try:
            self.label = QtWidgets.QLabel(self.playList[self.currentSongIndex],self.mp3)
        except:
            self.label = QtWidgets.QLabel('Eie Theme',self.mp3)
        self.label.setGeometry(10,10,600,100)
        font000 = QtGui.QFont()
        font000.setPointSize(40)
        self.label.setFont(font000)
        
        self.label2 = QtWidgets.QLabel('MHz',self.radio)
        self.label2.setGeometry(410,90,100,80)
        font000 = QtGui.QFont()
        font000.setPointSize(35)
        self.label2.setFont(font000)
        #
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
        self.Radio.setTabText(self.Radio.indexOf(self.radio), _translate("gui", "Radio"))
        self.actionabc.setText(_translate("gui", "abc"))

    def next(self, gui):
        if self.currentSongIndex+1<self.playListLengh:
            self.proc.send('n')
            self.currentSongIndex+=1
            try:
                self.label.setText(self.playList[self.currentSongIndex%playListLengh])
            except:
                self.label.setText('no song')   
        
    def previous(self, gui):
        self.proc.send('b')
        self.currentSongIndex-=1
        try:
            self.label.setText(self.playList[self.currentSongIndex%playListLengh])
        except:
            self.label.setText('no song')            

    def pause(self, gui):
        self.proc.send(' ')
        
    def play(self, gui):
        self.playing = True
        self.proc.send(' ')
        #self.label.setText('Button clicked.')
        
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
