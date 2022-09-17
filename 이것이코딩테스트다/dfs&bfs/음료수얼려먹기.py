from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    if graph[x][y] == 1:
        return False

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))

    return True


cnt = 0

for i in range(n):
    for j in range(m):
        if bfs(i, j):
            cnt += 1

print(cnt)
