# 0은 이동 가능 1은 벽
# (1,1)에서 (N,M)까지
# 시작하는 칸과 끝나는 칸도 포함하여 센다
# 벽 한 개는 부숴도 된다
from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]


def bfs():
    q = deque([(0, 0, 0)])
    visit[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny][wall] == 0:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, wall))
                    visit[nx][ny][wall] = visit[x][y][wall] + 1

                if wall == 0 and graph[nx][ny] == 1:
                    q.append((nx, ny, 1))
                    visit[nx][ny][1] = visit[x][y][wall] + 1

    return -1


print(bfs())
