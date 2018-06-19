import sys
playListPath = '/home/gab/Qt5/RadioGUI/pyqtradio-master/'


from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from radio import Ui_gui

class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_gui(playListPath)
		self.ui.setupUi(self)
		self.showFullScreen()

app = QApplication(sys.argv)
w = AppWindow()
w.showFullScreen()
sys.exit(app.exec_())


