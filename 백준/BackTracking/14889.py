import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
min_diff = int(1e9)


def dfs(depth, idx):
    global min_diff
    if depth == n // 2:
        start_sum, link_sum = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_sum += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link_sum += graph[i][j]
        min_diff = min(min_diff, abs(start_sum - link_sum))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False


dfs(0, 0)
print(min_diff)
