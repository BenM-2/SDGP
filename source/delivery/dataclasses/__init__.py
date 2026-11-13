"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          __init__.py
@Description:   This file contains custom data classes for the delivery package.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from algorithm.algorithm import floyd_warshall
# Third-party
import numpy as np  