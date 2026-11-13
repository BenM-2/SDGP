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
class DeliveryParsed:
    time_From_Headquarters:dict[str,int]
    internal_sector_times:list[dict[str,dict[str,int]]]


@dataclass
class AlgorithmPrecompute:
    parsed: DeliveryParsed
    graphs: list[dict[str, dict[str, int]]] = field(init=False, repr=False)
    shortest_times: dict[str, dict[str, int]] | None | np.ndarray = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self.graphs = self._build_graph()
        self.shortest_times = floyd_warshall(self.graphs)

    def _build_graph(self) -> list[dict[str, dict[str, int]]]:
        graph: list[dict[str, dict[str, int]]] = [{}]
        return graph



if __name__ == "__main__":
    parsed = DeliveryParsed(time_From_Headquarters= {},internal_sector_times=[{}])
    AlgorithmPrecompute(parsed)