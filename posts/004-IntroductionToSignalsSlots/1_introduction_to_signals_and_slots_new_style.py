#!/usr/bin/python
# 
# Bites Of Code
# 
# Introduction to Signals/Slots
# http://bitesofcode.blogspot.com/2011/10/introduction-to-signalsslots.html
# 

from PyQt4 import QtGui

class TestDialog(QtGui.QDialog):
    def __init__(self):
        super(TestDialog, self).__init__()

        testCombo = QtGui.QComboBox(self)
        testCombo.addItems(["Item 1", "Item 2"])
        
        # Create connection.
        testCombo.currentIndexChanged.connect(self.showResult)

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

