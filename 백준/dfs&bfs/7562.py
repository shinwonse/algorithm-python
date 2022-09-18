from collections import deque
import sys

input = sys.stdin.readline
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, 2, -2, 2, -2, 1, -1]


def bfs(sx, sy, ex, ey):
    queue = deque()
    queue.append([sx, sy])
    board[sx][sy] = 1
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            print(board[ex][ey] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                queue.append([nx, ny])
                board[nx][ny] = board[x][y] + 1


t = int(input())
for i in range(t):
    l = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    board = [[0] * l for _ in range(l)]
    bfs(start_x, start_y, end_x, end_y)
