from collections import deque
import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, alp):
    answer = 1
    queue = set([(y, x, alp)])

    while queue:
        print(queue)

        y, x, alp = queue.pop()
        answer = max(answer, len(alp))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < r and 0 <= nx < c and graph[ny][nx] not in alp:
                queue.add((ny, nx, alp + graph[ny][nx]))

    return answer


alp = graph[0][0]

print(bfs(0, 0, alp))
