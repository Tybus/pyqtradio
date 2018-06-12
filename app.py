import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from prueba3 import Ui_Radio

class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Radio()
		self.ui.setupUi(self)
		self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.showFullScreen()
sys.exit(app.exec_())
