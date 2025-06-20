from heapq import *
from math import inf


def dijkstra(n, graph, source, destination):
    dist = [inf] * n
    dist[source] = 0
    pq = [(0, source)]
    visited = set()

    while pq:
        curr_dist, curr_node = heappop(pq)
        for nei in graph[curr_node]:
            if nei not in visited:
                new_dist = curr_dist + graph[curr_node][nei]
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heappush(pq, (new_dist, nei))
        visited.add(curr_node)

    return dist[destination]


def dijkstra_grid(m, n, graph):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    dist = [[inf] * n for _ in range(m)]
    dist[0][0] = 0
    visited = set()
    pq = [(0, 0, 0)]

    while pq:
        curr_dist, i, j = heappop(pq)
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if (ni, nj) not in visited and 0 <= ni < m and 0 <= nj < n:
                new_dist = curr_dist + graph[ni][nj]
                if new_dist < dist[ni][nj]:
                    dist[ni][nj] = new_dist
                    heappush(pq, (new_dist, ni, nj))
        visited.add((i, j))

    return dist[-1][-1]
