import heapq


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for a, b, dist in paths:
        graph[a].append((b, dist))
        graph[b].append((a, dist))

    INF = int(1e9)
    q = []
    distance = [INF] * (n + 1)

    for start_node in gates:
        distance[start_node] = 0
        q.append((0, start_node))

    answer = []
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if now in summits:
            answer.append([distance[now], now])
            continue

        for to_node, add_dist in graph[now]:
            added_dist = max(distance[now], add_dist)
            if added_dist < distance[to_node]:
                distance[to_node] = added_dist
                heapq.heappush(q, (distance[to_node], to_node))

    answer.sort()
    return [answer[0][1], answer[0][0]]
