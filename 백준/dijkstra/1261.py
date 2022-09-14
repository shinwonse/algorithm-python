import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
a = []

for i in range(m):
    a.append(input())

dist = [[-1] * n for _ in range(m)]
dist[0][0] = 0
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q.append([0, 0])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if dist[nx][ny] == -1:
                if a[nx][ny] == "0":
                    q.appendleft([nx, ny])
                    dist[nx][ny] = dist[x][y]
                elif a[nx][ny] == "1":
                    q.append([nx, ny])
                    dist[nx][ny] = dist[x][y] + 1

print(dist[m - 1][n - 1])
