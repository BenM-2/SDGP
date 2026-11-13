"""
@Author:        George Dawson
@Date:          13/11/2026
@Name:          __init__.py
@Description:   This file is used to initialize the GUI package and import necessary modules.
"""

# Standard library
import os
import sys
from typing import Any, Optional

# Third-party libraries
import customtkinter as ctk

# Internal dependencies
from ..errors.errors import Errors, GUIError

__all__ = [
    "os",
    "sys",
    "Any",
    "Optional",
    "ctk",
    "Errors",
    "GUIError",
]