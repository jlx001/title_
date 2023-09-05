from ..app.function.progress_dialog import ProgressDialog

# from .app.function.progress_dialog import ProgressDialog

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    progressDialog = ProgressDialog()
    progressDialog.show()
    sys.exit(app.exec_())