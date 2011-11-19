#!/usr/bin/python
# 
# Bites Of Code
# 
# Comparison of Loading Techniques
# http://bitesofcode.blogspot.com/2011/10/comparison-of-loading-techniques.html
# 

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui_mainwindow import Ui_MainWindow

class SampleDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(SampleDialog, self).__init__(parent)
        self.setWindowTitle("Testing")
        self.resize(200, 100)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Load the ui.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Assign the actions.
        self.ui.ui_exec_btn.setDefaultAction(self.ui.ui_exec_act)
        self.ui.ui_show_btn.setDefaultAction(self.ui.ui_show_act)
        self.ui.ui_count_btn.setDefaultAction(self.ui.ui_count_act)

        # Create the connections.
        self.ui.ui_exec_act.triggered.connect(self.execDialog)
        self.ui.ui_show_act.triggered.connect(self.showDialog)
        self.ui.ui_count_act.triggered.connect(self.showCount)

    def execDialog(self):
        dlg = SampleDialog(self)
        dlg.exec_()

    def showDialog(self):
        dlg = SampleDialog(self)
        dlg.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dlg.show()

    def showCount(self):
        count = len(self.findChildren(QtGui.QDialog))
        QtGui.QMessageBox.information(self, "Dialog Count", str(count))

if __name__ == "__main__":
    app = None
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication([])

    window = MainWindow()
    window.show()

    if app:
        app.exec_()

