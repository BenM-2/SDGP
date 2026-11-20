"""
@Author:        George Dawson
@Date:          19/11/2026
@Name:          io_dc.py
@Description:   This file contains custom data classes for the delivery package I/O operations
"""

from . import *

@dataclass
class input_routes:
    filename: str

    # E.G: File input from CSV file
    """
    result = {
        "shift":[{
            "areas": ["Sectors"],
        }]
    } // Example of the expected structure
    """

    result: dict[int,
                 dict[str,
                      list[str]
                    ]
                ]


@dataclass
class input_distances:
    time_From_Headquarters: dict[str,int]
    """
    internal_Sector_Times = {
        "sector":[src,dest,time]
    } // Example of the expected structure
    """
    internal_Sector_Times:  dict[str,list[int]]



@dataclass
class output:
    filename: str
    result: None # dict[shift, dict[areas, trucks]] // expected output structure