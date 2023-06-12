import heapq
from Vertex import *


def dijkstra(graf, start):
    dist = {vertex: float('inf') for vertex in graf}
    dist[start] = 0
    queue = []

    heapq.heappush(queue, (0, start))

    visited = set()

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graf[current_vertex].items():
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return dist