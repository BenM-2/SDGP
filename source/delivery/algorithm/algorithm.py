"""
@Author:        Ben Marples
@Date:          13/11/2026
@Name:          algorithm.py
@Description:   Flow of data is delivery_data -> delivery_digest -> algorithm_data_class
"""

from . import *
import datetime

def floyd_warshall(edges:list[list[int]],n:int) -> floyd_result:
    """Run Floyd-Warshall on a graph.

    :param edges: Edge list describing the graph.
    :param n: Number of nodes.
    :return: Shortest-path result for all node pairs.
    """
    dist = np.full((n,n),np.inf)
    path = np.full((n,n),-1,dtype=np.int_)

    for src,dest,time in edges:
        a, b = src - 1, dest - 1
        if time < dist[a][b]:                    # keeps the cheapest if edges repeat
            dist[a][b] = dist[b][a] = time
            path[a][b] = a                       # predecessor of b on a -> b
            path[b][a] = b                       # predecessor of a on b -> a

    np.fill_diagonal(dist,0)

    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]

    return floyd_result(distance_table=dist,path_table=path)

def get_path(fr:floyd_result,src:int,dest:int)->list[int]:
    """Get the shortest path between two nodes.

    :param fr: Dataclass containing a distance and path_table
    :param src: Starting node. (zero indexed) 
    :param dest: Destination node. (zero indexed)
    :return: Nodes along the path from ``src`` to ``dest``.
    """
    if fr.path_table[src][dest] == -1:
        return []
    path = [dest]
    while dest != src:
        dest = int(fr.path_table[src][dest])
        path.append(dest)
    path.reverse()
    return path

if __name__ == "__main__":
    # edges = [
    #     ["A1", "A2", 7],
    #     ["A2", "A3", 6],
    #     ["A1", "A4", 5],
    #     ["A2", "A4", 5],
    #     ["A4", "A5", 7],
    #     ["A5", "A6", 7],
    #     ["A3", "A6", 5],
    # ]
    edges = [
        [1, 2, 7],
        [2, 3, 6],
        [1, 4, 5],
        [2, 4, 5],
        [4, 5, 7],
        [5, 6, 7],
        [3, 6, 5],
    ]
    edges2 = [
        [1, 2, 5], [2, 3, 5], [1, 4, 5], [1, 5, 7],
        [5, 6, 5], [5, 7, 6], [1, 8, 5], [2, 9, 5],
        [4, 10, 7], [10, 11, 5], [9, 12, 5], [12, 13, 7],
        [12, 14, 7], [7, 15, 5], [8, 16, 7], [9, 17, 5],
        [6, 18, 7], [14, 19, 6], [9, 20, 5], [7, 21, 6],
        [4, 22, 5], [13, 23, 5], [12, 24, 6], [20, 25, 6],
        [2, 26, 7], [15, 27, 7], [4, 28, 6], [3, 29, 7],
        [10, 30, 7], [20, 31, 6], [19, 32, 5], [5, 33, 5],
        [15, 34, 6], [6, 35, 5], [7, 36, 6], [18, 37, 6],
        [24, 38, 5], [24, 39, 6], [14, 40, 7], [18, 41, 7],
        [5, 42, 7], [41, 43, 5], [35, 44, 7], [16, 45, 5],
        [30, 46, 6], [18, 47, 7], [45, 48, 7], [15, 49, 7],
        [21, 50, 5], [15, 51, 5], [21, 52, 6], [18, 53, 5],
        [14, 54, 7], [46, 55, 6], [14, 56, 7], [32, 57, 6],
        [57, 58, 7], [30, 59, 5], [17, 60, 5], [16, 61, 7],
        [36, 62, 7], [17, 63, 7], [38, 64, 6], [52, 65, 6],
        [29, 66, 5], [66, 67, 6], [12, 68, 5], [15, 69, 5],
        [21, 70, 7], [55, 71, 7], [9, 72, 6], [49, 73, 7],
        [60, 74, 7], [33, 75, 7], [2, 76, 7], [15, 77, 7],
        [69, 78, 6], [44, 79, 5], [38, 80, 6], [21, 81, 6],
        [1, 82, 7], [34, 83, 7], [23, 84, 7], [14, 85, 7],
        [39, 86, 7], [65, 87, 7], [26, 88, 5], [48, 89, 5],
        [70, 90, 7], [1, 91, 7], [42, 92, 6], [3, 93, 5],
        [47, 94, 6], [31, 95, 5], [31, 96, 7], [11, 97, 5],
        [94, 98, 6], [9, 99, 7], [99, 100, 5], [17, 85, 6],
        [22, 71, 6], [68, 78, 6], [28, 70, 7], [26, 89, 7],
        [40, 52, 7], [48, 84, 6], [58, 67, 5], [29, 32, 5],
        [3, 44, 7], [30, 71, 7], [1, 29, 5], [81, 91, 5],
        [9, 30, 5], [10, 43, 7], [31, 36, 7], [28, 63, 7],
        [17, 93, 7], [61, 74, 5], [53, 61, 5], [13, 85, 6],
        [53, 60, 7], [7, 87, 7], [13, 83, 5], [52, 94, 6],
        [14, 32, 5], [25, 69, 6], [18, 55, 5], [36, 60, 5],
        [10, 57, 7], [7, 13, 7], [2, 70, 5], [31, 97, 5],
        [53, 63, 6], [28, 52, 5], [22, 49, 5], [34, 50, 6],
        [37, 55, 7], [72, 94, 7], [63, 92, 5], [25, 38, 5],
        [8, 75, 7], [8, 70, 7], [8, 41, 5], [62, 75, 7],
        [21, 68, 5], [11, 66, 5], [9, 77, 5], [31, 87, 6],
        [16, 73, 5], [75, 77, 5], [11, 80, 6], [75, 85, 7],
        [41, 67, 6], [27, 86, 7], [31, 41, 6], [17, 51, 7],
        [39, 83, 6], [41, 97, 5], [2, 59, 7], [13, 73, 5],
        [28, 69, 7], [17, 34, 6], [9, 32, 6], [21, 37, 6],
        [70, 91, 6], [79, 84, 7], [2, 86, 7], [39, 85, 5],
        [18, 34, 5], [14, 96, 7], [20, 35, 6], [27, 78, 7],
        [27, 44, 7], [34, 82, 7], [33, 63, 5], [12, 82, 6],
        [6, 36, 5], [43, 99, 5], [21, 95, 6], [71, 91, 6],
        [2, 72, 5], [10, 89, 5], [5, 70, 6], [71, 75, 5],
        [17, 56, 5], [40, 47, 5], [27, 46, 7], [32, 86, 5],
        [46, 100, 7], [53, 80, 7], [21, 23, 6], [4, 23, 7],
        [43, 53, 7], [32, 95, 6], [21, 90, 5], [5, 49, 6],
        [26, 29, 6], [40, 45, 5], [4, 29, 7],
    ]

    n1 = 0
    for u,t,d in edges:
        if u > n1:
            n1 = u
        if t > n1:
            n1 = t
    
    start1 = datetime.datetime.now()
    x = floyd_warshall(edges,n1)
    print(x)
    for src in range(0,6):
        for dest in range(0,6):
                print(f"Src:{src +1},Dest:{dest+1},{get_path(x,src,dest)}")
    end1 = datetime.datetime.now()
    # n2 = 0
    # for u,t,d in edges2:
    #     if u > n2:
    #         n2 = u
    #     if t > n2:
    #         n2 = t
    # start2 = datetime.datetime.now()
    # floyd_warshall_test(edges2,n2)
    # end2 = datetime.datetime.now()
    # d1 = (end1 - start1).total_seconds()
    # d2 = (end2 - start2).total_seconds()

    # result = d2 / d1
    # print(f"\nedges1 took {d1}\nedges2 took {d2}\ntime difference {abs((d1) - (d2))}\n edges 2 is {result} times slower and array is {n2 / n1} times biger")



