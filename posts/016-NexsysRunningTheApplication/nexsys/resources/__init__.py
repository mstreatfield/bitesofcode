""" 
Provides methods to access various resource files for the application.
"""

# define authorship information
__authors__     = ["Mark Streatfield"]
__author__      = ",".join(__authors__)
__credits__     = [
        ("Oxygen Team", "New Text File Icon (GNU/GPL from findicons.com)"),
]
__copyright__   = "Copyright (c) 2011"
__license__     = "GPL"

# maintanence information
__maintainer__  = "Mark Streatfield"
__email__       = 'mstreatfield@gmail.com'

import os.path

BASE_PATH = os.path.dirname(__file__)

def find(relpath):
    """
    Looks up the resource file based on the relative path to this module.
    """
    return os.path.join(BASE_PATH, relpath)

