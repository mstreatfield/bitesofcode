""" 
Sub-package containing all user interface components for nexsys.
"""

# define authorship information
__authors__     = ["Mark Streatfield"]
__author__      = ",".join(__authors__)
__credits__     = ["Eric Hulser"]
__copyright__   = "Copyright (c) 2011"
__license__     = "GPL"

# maintanence information
__maintainer__  = "Mark Streatfield"
__email__       = "mstreatfield@gmail.com"

import os.path

import PyQt4.uic
from PyQt4 import QtCore

def loadUi(modpath, widget):
    """
    Uses the PyQt4.uic.loadUi method to load the inputted ui file associated
    with the given module path and widget cladd information on the inputted
    widget
    """
    # Generate the uifile path.
    basepath = os.path.dirname(modpath)
    basename = widget.__class__.__name__.lower()
    uifile = "%s.ui" % basename
    uipath = os.path.join(basepath, "ui")

    # Swap the current path to use the ui file's path.
    currdir = QtCore.QDir.currentPath()
    QtCore.QDir.setCurrent(uipath)

    # Load the ui.
    PyQt4.uic.loadUi(uifile, widget)

    # Reset the current QDir path.
    QtCore.QDir.setCurrent(currdir)

