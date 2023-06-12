from Vertex import *


def tworzenie_grafu():
    g = Gr()

    n_ver = int(input("Podaj ilość wierzchołków: "))
    for i in range(n_ver):
        key = input("Podaj identyfikatory wierzchołków: ")
        g.addVertex(key)

    n_edges = int(input("Podaj ilość krawędzi: "))
    for i in range(n_edges):
        from_vertex = input("Podaj wierzchołek początkowy: ")
        to_vertex = input("Podaj wierzchołek końcowy: ")
        cost = int(input("Podaj wagę krawędzi: "))
        g.addEdge(from_vertex, to_vertex, cost)

    return g


gr = tworzenie_grafu()

print("Wierzchołki: ")
for vertex in gr.getVertices():
    print(vertex)

print("Krawędzi: ")
for vertex in gr:
    for neighbor in vertex.getConnections():
        print(f"{vertex.getId()} --> {neighbor.getId()} (waga: {vertex.getWeight(neighbor)})")