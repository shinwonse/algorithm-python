import sys

input = sys.stdin.readline

# 입력 받기
R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input()))

direction = [(-1, 1), (0, 1), (1, 1)]


def pipe(x, y):
    global answer
    graph[x][y] = "x"
    if y == C - 1:
        answer += 1
        return True
    for k in range(3):
        nx = x + direction[k][0]
        ny = y + direction[k][1]
        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] == ".":
                if pipe(nx, ny):
                    return True


answer = 0
for i in range(R):
    pipe(i, 0)
print(answer)
