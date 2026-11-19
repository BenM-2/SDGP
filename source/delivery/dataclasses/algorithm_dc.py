"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          algorithm_dc.py
@Description:   This file contains custom data classes for the delivery package.
"""

from . import *

"""
x = {
    "A1":[["A2",7],["AX",time]]
}
"""


@dataclass
class AlgorithmPrecompute:
    parsed: input_distances
    graphs: list[dict[str, dict[str, int]]] = field(init=False, repr=False)
    shortest_times: dict[str, dict[str, int]] | None | np.ndarray = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self.graphs = self._build_graph()
        self.shortest_times = floyd_warshall(self.graphs)

    def _build_graph(self) -> list[dict[str, dict[str, int]]]:
        graph: list[dict[str, dict[str, int]]] = [{}]
        return graph



if __name__ == "__main__":
    parsed = input_distances(time_From_Headquarters= {},internal_Sector_Times=[{}])
    x = AlgorithmPrecompute(parsed)

    print(x)