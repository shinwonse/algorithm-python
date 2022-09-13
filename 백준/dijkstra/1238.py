import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)

    # 시작점은 거리 0으로 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 거리, 현재 노드
        dist, now = heapq.heappop(q)
        # 현재 노드의 거리 메모이제이션 정보가 지금 거리보다 작으면 이미 갱신된것
        if distance[now] < dist:
            continue

        # 현재 노드의 인접 노드 탐색
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    # x로 가는 최단거리 + 출발점 i로 돌아오는 최단거리
    result = max(result, go[x] + back[i])

print(result)
