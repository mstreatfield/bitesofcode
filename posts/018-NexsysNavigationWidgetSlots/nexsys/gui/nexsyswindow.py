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
        
        # Define custom properties.
        self._currentNavigationWidget = None

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

        self.ui_goup_act.triggered.connect(self.goUp)
        self.ui_goroot_act.triggered.connect(self.goToRoot)
        self.ui_gohome_act.triggered.connect(self.goHome)

        app = QtGui.QApplication.instance()
        app.focusChanged.connect(self.updateCurrentNavigationWidget)

    def createNewFile(self):
        """
        Prompts the user to enter a new file name to create at the current
        path.
        """
        QtGui.QMessageBox.information(self, "Create File", "Create New Text File")
    
    def currentNavigationWidget(self):
        """
        Returns the currently active navigation widget.  A user can control
        which widget is curent by assigning focus to it's children.
        """
        return self._currentNavigationWidget
    
    def goHome(self):
        """
        Navigate to the user's home path for the current navigation widget.
        Will return False if there is no widget found.
        """
        widget = self.currentNavigationWidget()
        if not widget:
            return False
        
        widget.goHome()
        return True
    
    def goToRoot(self):
        """
        Navigate up to the root path for the current navigation widget.
        Will return False if there is no widget found.
        """
        widget = self.currentNavigationWidget()
        if not widget:
            return False
        
        widget.goToRoot()
        return True
    
    def goUp(self):
        """
        Navigates up the folder hierarchy for the current navigation widget.
        Will return False if there is no widget found.
        """
        widget = self.currentNavigationWidget()
        if not widget:
            return False
        
        widget.goUp()
        return True
    
    def setCurrentNavigationWidget(self, widget):
        """
        Sets the currently active navigation widget to the inputted widget.
        """
        if widget == self._currentNavigationWidget:
            return False
        
        self._currentNavigationWidget = widget
        self.updateCommandPath()
        return True
    
    def updateCommandPath(self):
        """
        Updates the command line widget's path to reflect the current path
        for the current navigation widget.
        """
        widget = self.currentNavigationWidget()
        if not widget:
            return
        
        self.ui_cmdline_lbl.setText(widget.currentPath() + " ")

    def updateCurrentNavigationWidget(self, oldWidget, newWidget):
        """
        Lookup the parent of the focused widget for our navigation widgets.
        """
        # Make sure we have a new widget that is focused.
        if not newWidget:
            return
        
        # Check to see if the newly focused widget is a member of a 
        # NavigationWidget class
        parentWidget = newWidget.parentWidget()
        if isinstance(parentWidget, NavigationWidget):
            self.setCurrentNavigationWidget(parentWidget)

