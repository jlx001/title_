from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem, QListWidget, QDialog
from app.view.Ui_downloading import Ui_downloading
import sys

class downloadingDialog(QDialog, Ui_downloading):
    def __init__(self, parent=None):
        super(downloadingDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('下載')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_downloading()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
