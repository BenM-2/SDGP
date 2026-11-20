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
    graphs: list[dict[str, dict[str, int]]] = field(init=False, repr=False)
    shortest_times: dict[str, dict[str, int]] | None | np.ndarray = field(init=False, repr=False)
    
    def __post_init__(self) -> None:
        self.graphs = self._build_graph()
        self.shortest_times = floyd_warshall(self.graphs)

    def _build_graph(self) -> list[dict[str, dict[str, int]]]:
        graph: list[dict[str, dict[str, int]]] = [{}]
        return graph

