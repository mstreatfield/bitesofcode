#!/usr/bin/python
# 
# Bites Of Code
# 
# Introduction to Layouts
# http://bitesofcode.blogspot.com/2011/10/introduction-to-layouts.html
# 

from PyQt4 import QtGui
from PyQt4 import QtCore

class SampleDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(SampleDialog, self).__init__(parent)
        self.setWindowTitle("Testing")
        self.resize(200, 100)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Create the menu.
        test_menu = self.menuBar().addMenu("Testing")

        # Create the menu actions.
        exec_act = test_menu.addAction("Exec Dialog")
        show_act = test_menu.addAction("Show Dialog")
        count_act = test_menu.addAction("Show Count")

        # Create the tool buttons.
        exec_btn = QtGui.QToolButton(self)
        show_btn = QtGui.QToolButton(self)
        count_btn = QtGui.QToolButton(self)

        # Layout the buttons horizontally
        layout = QtGui.QHBoxLayout()
        layout.addStretch()
        layout.addWidget(exec_btn)
        layout.addWidget(show_btn)
        layout.addWidget(count_btn)

        # Create the central container widget.
        widget = QtGui.QWidget(self)

        # Create vertical layout and stretch
        vlayout = QtGui.QVBoxLayout()
        vlayout.addStretch()
        vlayout.addLayout(layout)

        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

        # Assign the actions.
        exec_btn.setDefaultAction(exec_act)
        show_btn.setDefaultAction(show_act)
        count_btn.setDefaultAction(count_act)

        # Create the connections.
        exec_act.triggered.connect(self.execDialog)
        show_act.triggered.connect(self.showDialog)
        count_act.triggered.connect(self.showCount)

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

