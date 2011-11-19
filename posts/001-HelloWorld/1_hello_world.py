#!/usr/bin/python
# 
# Bites Of Code
# 
# Hello, World
# http://bitesofcode.blogspot.com/2011/10/hello-world.html
# 

from PyQt4 import QtGui

if __name__ == "__main__":
    # Define application pointer in case we create our own.
    app = None
    
    # Check to see if there is already a QApplication
    # instance defined somewhere.
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication([])
    
    # Popup a new dialog.
    QtGui.QMessageBox.information(None, "Hello", "Hello, World!")

