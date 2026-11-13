"""
@Author:        George Dawson
@Date:          13/11/2026
@Name:          __init__.py
@Description:   This file serves as the initialization module for the delivery package.
"""

# Errors
from .errors.errors import (
    Errors,
    AlgorithmError,
    GUIError,
    ParsingError,
    GenericError,
)

# GUI
from .gui.gui import (
    Gui,
)

# Algorithms
# Add imports once algorithm modules are created.
# from .algorithm.algorithm_dc import Route, DeliveryResult

# Delivery parsing
# from .delivery_parsing.parser import DeliveryParser

# Route parsing
# from .route_parsing.parser import RouteParser


__all__ = [
    # Errors
    "Errors",
    "AlgorithmError",
    "GUIError",
    "ParsingError",
    "GenericError",

    # GUI
    "Gui",

    # Algorithms
    # "Route",
    # "DeliveryResult",

    # Delivery parsing
    # "DeliveryParser",

    # Route parsing
    # "RouteParser",
]