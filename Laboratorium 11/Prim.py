import heapq
from Laboratorium_9.Vertex import *


def prim(graph):
    MRT = []
    start_vertex = next(iter(graph))
    visited = set([start_vertex])
    krawedzie = [(waga, start_vertex, sasiad) for sasiad, waga in start_vertex.connectedTo.items()]
    heapq.heapify(krawedzie)

    while krawedzie:
        waga, current_vertex, next_vertex = heapq.heappop(krawedzie)
        if next_vertex not in visited:
            visited.add(next_vertex)
            MRT.append((current_vertex.getId(), next_vertex.getId(), waga))
            for sasiad, waga in next_vertex.connectedTo.items():
                if sasiad not in visited:
                    heapq.heappush(krawedzie, (waga, next_vertex, sasiad))

    return MRT