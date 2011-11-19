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
        
        # Create components.
        testCombo = QtGui.QComboBox(self)
        testCombo.addItems(["Item 1", "Item 2"])
        
        emitButton = QtGui.QPushButton("Emit Signal", self)
        
        # Create the layout.
        layout = QtGui.QVBoxLayout()
        layout.addWidget(testCombo)
        layout.addWidget(emitButton)
        
        self.setLayout(layout)
        
        # Store the combo.
        self._testCombo = testCombo
        
        # Store the connections.
        self.connect(testCombo, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.showResult)
        emitButton.clicked.connect(self.emitChangeSignal)

    def emitChangeSignal(self):
        self._testCombo.emit(QtCore.SIGNAL("currentIndexChanged(const QString&)"), self._testCombo.currentText())

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

