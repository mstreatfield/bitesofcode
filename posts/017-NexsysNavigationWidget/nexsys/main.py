""" 
Main entry point to the nexsys application.
"""

# define authorship information
__authors__     = ["Mark Streatfield"]
__author__      = ",".join(__authors__)
__credits__     = ["Eric Hulser"]
__copyright__   = "Copyright (c) 2011"
__license__     = "GPL"

# maintanence information
__maintainer__  = "Mark Streatfield"
__email__       = "mark.streatfield@gmail.com"

from PyQt4 import QtGui

def main(argv=None):
    """
    Creates the main window for the nexsys application and begins the
    QApplication if necessary.
    """
    app = None

    if argv is None:
        argv = []

    # Create the application if necessary.
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication(argv)
        app.setStyle("plastique")

    # Create the main window.
    from nexsys.gui.nexsyswindow import NexsysWindow
    window = NexsysWindow()
    window.show()

    # Run the application if necessary.
    if app:
        return app.exec_()
    
    # No errors since we're not running our own event loop.
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main(sys.argv))

