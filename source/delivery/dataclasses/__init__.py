"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          __init__.py
@Description:   This file contains custom data classes for the delivery package.
"""
from __future__ import annotations
from dataclasses import dataclass,field
from typing import Callable, IO, TextIO
from ..algorithm.algorithm import floyd_warshall
from ..dataclasses.io_dc import * # do as i say not as i do :)
# Third-party
import numpy as np
import csv


from .algorithm_dc import AlgorithmPrecompute

__all__ = [
    "annotations",
    "dataclass",
    "field",
    "Callable",
    "floyd_warshall",
    "np",
    "AlgorithmPrecompute",
    "input_routes",
    "input_distances",
]