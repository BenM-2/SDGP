"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          gui_dc.py
@Description:   This file contains custom data classes for the delivery package.
"""

from . import *

@dataclass
class gui_cb:
    tab_cb: Callable
    close_cb: Callable
    algorithms_cb:Callable
    