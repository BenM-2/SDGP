"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          algorithm.py
@Description:   Flow of data is delivery_data -> delivery_digest -> algorithm_data_class
"""

from . import *


def example_algorithm():
    raise AlgorithmError(
        AlgorithmErrorCode.Err_Graph_Invalid,
        "Graph is invalid"
    )

def floyd_warshall(graph_network: list[dict[str, dict[str, int]]]) -> np.ndarray :
    x = np.ndarray(shape=1)
    return x