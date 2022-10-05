import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    # 이미 방문한 적이 있을 경우
    if dp[x][y] != -1:
        return dp[x][y]

    # Base case
    if x == M - 1 and y == N - 1:
        return 1

    # Recursive case
    dp[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx <= M - 1 and 0 <= ny <= N - 1:
            if nums[x][y] > nums[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]


M, N = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
print(dfs(0, 0))
