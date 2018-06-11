import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from prueba1 import Radio

class AppWindow(QDialog):
	def __init__(self):
		super().__init__()
		self.ui = Radio()
		self.ui.setupUi(self)
		self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
