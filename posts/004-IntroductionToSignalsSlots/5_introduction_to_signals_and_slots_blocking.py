#!/usr/bin/python
# 
# Bites Of Code
# 
# Introduction to Signals/Slots
# http://bitesofcode.blogspot.com/2011/10/introduction-to-signalsslots.html
# 

from PySide import QtGui
from PySide import QtCore

class TestDialog(QtGui.QDialog):
    def __init__(self):
        super(TestDialog, self).__init__()

        # Create components.
        self._checkA = QtGui.QCheckBox("Check 01", self)
        self._checkB = QtGui.QCheckBox("Check 02", self)

        # Create the layout.
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self._checkA)
        layout.addWidget(self._checkB)

        self.setLayout(layout)

        # Create connections
        self._checkA.toggled.connect(self.setCheckA)
        self._checkB.toggled.connect(self.setCheckB)

    def setCheckA(self, state):
        # Block signals.
        self._checkA.blockSignals(True)
        self._checkB.blockSignals(True)

        # Modify checkboxes.
        self._checkA.setChecked(True)
        self._checkB.setChecked(False)
        
        # Unblock signals.
        self._checkA.blockSignals(False)
        self._checkB.blockSignals(False)

    def setCheckB(self, state):
        # Block signals.
        self._checkA.blockSignals(True)
        self._checkB.blockSignals(True)

        # Modify checkboxes.
        self._checkA.setChecked(False)
        self._checkB.setChecked(True)
                                                        
        # Unblock signals.
        self._checkA.blockSignals(False)
        self._checkB.blockSignals(False)

if __name__ == "__main__":
    app = None
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication([])
    
    dlg = TestDialog()
    dlg.show()

    if app:
        app.exec_()

