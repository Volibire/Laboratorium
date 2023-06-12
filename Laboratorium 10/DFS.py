from Laboratorium_9.Vertex import *


def dfs(graph):
    for vertex in graph.getVertices():
        vertex.p = -1
        vertex.visited = False

    time = 0

    for vertex in graph.getVertices():
        if not vertex.visited:
            time = DFS_EX(vertex, time)


def DFS_EX(vertex, time):
    time += 1
    vertex.time_1 = time
    vertex.visited = True

    for neighbor in vertex.getConnections():
        if not neighbor.visited:
            neighbor.p = vertex
            time = DFS_EX(neighbor, time)

    time += 1
    vertex.time_2 = time

    return time