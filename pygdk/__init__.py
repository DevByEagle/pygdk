"""
"""

def _attribute_undefined(name):
    raise RuntimeError(f"{name} is not available")

from pygdk.base import *

import pygdk.math
Vector2 = pygdk.math.Vector2

try:
    import pygdk.draw
except (ImportError, OSError):
    raise ModuleNotFoundError("The module named 'draw' is missing. Please ensure the module is correctly installed")

try:
    import pygdk.font
except (ImportError, OSError):
    raise ModuleNotFoundError("The module named 'font' is missing. Please ensure the module is correctly installed")

try:
    from pygdk.surface import Surface
except (ImportError, OSError):
    _attribute_undefined("pygdk.surface")

del pygdk
