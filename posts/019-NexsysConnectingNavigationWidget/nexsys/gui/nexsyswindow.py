""" 
Defines the main NexsysWindow class.
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

import nexsys.gui
from nexsys.gui.navigationwidget import NavigationWidget
from PyQt4 import QtGui

class NexsysWindow(QtGui.QMainWindow):
    """
    Main window class for the nexsys filesystem application.
    """

    def __init__(self, parent=None):
        super(NexsysWindow, self).__init__(parent)

        # Load the ui.
        nexsys.gui.loadUi(__file__, self)
        
        # Clear out the current tabs.
        self.ui_left_tab.clear()
        self.ui_right_tab.clear()

        # Hide the headers.
        self.ui_left_tab.tabBar().hide()
        self.ui_right_tab.tabBar().hide()

        # Create the default tabs.
        self.ui_left_tab.addTab(NavigationWidget(self), "")
        self.ui_right_tab.addTab(NavigationWidget(self), "")

        # Create connections.
        self.ui_newfile_act.triggered.connect(self.createNewFile)

    def createNewFile(self):
        """
        Prompts the user to enter a new file name to create at the current
        path.
        """
        QtGui.QMessageBox.information(self, "Create File", "Create New Text File")

