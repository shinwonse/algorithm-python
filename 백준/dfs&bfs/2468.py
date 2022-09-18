import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

min_area = min(map(min, graph))
max_area = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, safe_area):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] >= safe_area and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


max_safe_area = min_area
for safe_area in range(min_area, max_area + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= safe_area and visited[i][j] is False:
                bfs(i, j, safe_area)
                count += 1
        if count > max_safe_area:
            max_safe_area = count
print(max_safe_area)
