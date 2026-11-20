"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          algorithm_dc.py
@Description:   This file contains custom data classes for the delivery package.
"""

from . import np,npt,dataclass,input_distances,field,floyd_warshall

def format_table(table: npt.NDArray, title: str = "") -> str:
    n_rows, n_cols = table.shape

    def cell(v: object) -> str:
        if isinstance(v, (float, np.floating)):
            return "inf" if np.isinf(v) else f"{v:g}"
        return str(v)

    cells = [[cell(v) for v in row] for row in table]
    longest = max(len(c) for row in cells for c in row)
    width = max(longest, len(str(n_cols))) + 2  # column width incl. padding
    label_w = len(str(n_rows))                  # row-label width

    header = " " * label_w + "".join(f"{j + 1:>{width}}" for j in range(n_cols))
    rows = [
        f"{i + 1:<{label_w}}" + "".join(f"{c:>{width}}" for c in row)
        for i, row in enumerate(cells)
    ]
    lines = [header, *rows]
    return "\n".join([title, *lines] if title else lines)

@dataclass
class floyd_result:
    distance_table : npt.NDArray[np.float64]
    path_table : npt.NDArray[np.int_]

    def __str__(self) -> str:
        return (
            format_table(self.distance_table, "Distances:")
            + "\n\n"
            + format_table(self.path_table, "Paths:")
        )


@dataclass
class AlgorithmPrecompute:
    parsed: input_distances
    graph: list[list[list[int]]] = field(init=False, repr=False)
    shortest_times: list[floyd_result] = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self.graphs = self._build_graphs()
        for graph in self.graphs:
            n = 0
            for u,t,d in graph:
                if u > n:
                    n = u
                if t > n:
                    n = t
            self.shortest_times.append(floyd_warshall(graph,n)) 

    def _build_graphs(self) -> list[list[list[int]]] :
        graph: list[list[list[int]]] = []
        for key in self.parsed.internal_Sector_Times

        return graph

edges = [
        [1, 2, 7],
        [2, 3, 6],
        [1, 4, 5],
        [2, 4, 5],
        [4, 5, 7],
        [5, 6, 7],
        [3, 6, 5],
    ]