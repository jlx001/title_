from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QDialog
from ..view.Ui_progress import Ui_progressDialog


class ProgressDialog(QDialog, Ui_progressDialog):
    def __init__(self, parent=None):
        super(ProgressDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('下载')
        self.listWidget.itemClicked.connect(self.item_clicked)
        
    
    # 下载切换
    def item_clicked(self, item):
        # 获取当前选中的item
        item = self.listWidget.selectedItems()[0]
        if item.text() == '正在下载':
            self.stackedWidget.setCurrentIndex(1)
        if item.text() == '已完成':
            self.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    progressDialog = ProgressDialog()
    progressDialog.show()
    sys.exit(app.exec_())