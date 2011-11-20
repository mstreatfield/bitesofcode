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

import os.path
import PyQt4.uic
from PyQt4 import QtGui

class NexsysWindow(QtGui.QMainWindow):
    """
    Main window class for the nexsys filesystem application.
    """

    def __init__(self, parent=None):
        super(NexsysWindow, self).__init__(parent)

        # Load the ui.
        basepath = os.path.dirname(__file__)
        basename = self.__class__.__name__.lower()
        uifile   = os.path.join(basepath, 'ui/%s.ui' % basename)
        PyQt4.uic.loadUi(uifile, self)

