from collections import deque

INF = int(1e9)

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

shark_size = 2
now_x, now_y = 0, 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    dist = [[-1] * N for _ in range(N)]
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if dist[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(N):
        for j in range(N):
            # 도달 가능하면서 먹을 수 있을 때
            if dist[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x, y, min_dist  # 먹을 물고기 위치와 최단 거리


result = 0
ate = 0

while True:
    value = find(bfs())
    if value is None:
        print(result)
        break
    else:
        now_x, now_y = value[0], value[1]
        result += value[2]
        graph[now_x][now_y] = 0
        ate += 1
        if ate >= shark_size:
            shark_size += 1
            ate = 0
