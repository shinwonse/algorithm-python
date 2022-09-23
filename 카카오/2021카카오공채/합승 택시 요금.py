import heapq


def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        else:
            distance[now] = dist
        for dest in graph[now]:
            heapq.heappush(q, (dist + dest[1], dest[0]))
    return distance


def solution(n, s, a, b, fares):
    INF = int(1e9)
    minimum = INF
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))

    distance = dijkstra(s, distance, graph)
    for start in range(n + 1):
        dist = [INF] * (n + 1)
        dist = dijkstra(start, dist, graph)
        minimum = min(minimum, distance[start] + dist[a] + dist[b])
    return minimum
