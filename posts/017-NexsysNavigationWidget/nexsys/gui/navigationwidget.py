""" 
Defines the main NavigationWidget class.
"""

# define authorship information
__authors__     = ["Mark Streatfield"]
__author__      = ",".join(__authors__)
__credits__     = []
__copyright__   = "Copyright (c) 2011"
__license__     = "GPL"

# maintanence information
__maintainer__  = "Mark Streatfield"
__email__       = "mstreatfield@gmail.com"

import os.path
import nexsys.gui

from PyQt4 import QtGui
from PyQt4 import QtCore

class NavigationWidget(QtGui.QWidget):
    """
    Creates a reusable file navigation widget to move around between 
    different folders and files.
    """

    def __init__(self, parent=None, path=""):
        super(NavigationWidget, self).__init__(parent)
                            
        # load the ui
        nexsys.gui.loadUi(__file__, self)
                                                    
        # create the main filesystem model
        self._model = QtGui.QFileSystemModel(self)
        self._model.setRootPath("")
                                                                                    
        # determine the version of Qt to know if the QFileSystemModel is 
        # available for use yet
        if int(QtCore.QT_VERSION_STR.split(".")[1]) < 7:
            completer = QtGui.QCompleter(QtGui.QDirModel(self), self)
        else:
            completer = QtGui.QCompleter(self._model, self)
                                                                                                                                                                    
        # set the completion and model information
        self.ui_path_edit.setCompleter(completer)
        self.ui_contents_treev.setModel(self._model)
                                                                                                                                                                                                    
        # assign the default path
        self.setCurrentPath(path)
                                                                                                                                                                                                                            
        # create the connections
        self.ui_path_edit.returnPressed.connect(self.applyCurrentPath)

    def applyCurrentPath(self):
        """
        Assigns the current path from the text edit as the current path
        for the widget.
        """
        self.setCurrentPath(self.ui_path_edit.text())

    def currentPath(self):
        """
        Returns the current path that is assigned to this widget.
        """
        return str(self.ui_path_edit.text())
    
    def setCurrentPath(self, path):
        """
        Sets the current path for this widget to the inputted path, updating
        the tree and line edit to reflect the new path.
        """
        # Update the line edit to the latest path.
        self.ui_path_edit.setText(os.path.normpath(str(path)))

        # Shift the treeview to display contents from the new path root.
        index = self._model.index(path)
        self.ui_contents_treev.setRootIndex(index)

