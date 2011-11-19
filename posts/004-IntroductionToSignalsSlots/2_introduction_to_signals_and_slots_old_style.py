#!/usr/bin/python
# 
# Bites Of Code
# 
# Introduction to Signals/Slots
# http://bitesofcode.blogspot.com/2011/10/introduction-to-signalsslots.html
# 

from PyQt4 import QtGui
from PyQt4 import QtCore

class TestDialog(QtGui.QDialog):
    def __init__(self):
        super(TestDialog, self).__init__()

        testCombo = QtGui.QComboBox(self)
        testCombo.addItems(["Item 1", "Item 2"])
        
        # Create connection.
        self.connect(testCombo, QtCore.SIGNAL("currentIndexChanged(const QString &)"), self.showResult)

    def showResult(self, current):
        QtGui.QMessageBox.critical(self, "Results", str(current))

if __name__ == "__main__":
    app = None
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication([])
    
    dlg = TestDialog()
    dlg.show()

    if app:
        app.exec_()

