import sys
from PyQt5.QtWidgets import QApplication
from mainForm import mainFrom

app = QApplication(sys.argv)
win = mainFrom()
win.show()
sys.exit(app.exec_())