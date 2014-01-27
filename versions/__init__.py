__version__ = '0.7.0'

# We rely on cmp() which is not available in python 3
import sys

MAJOR = sys.version_info[0] 

if MAJOR == 3:
    cmp = lambda a, b: (a > b) - (a < b)  # pragma: no cover

from .api import *
