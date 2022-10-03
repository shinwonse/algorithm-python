# i번째 집을 1번째 색으로 칠하는 최소 비용의 경우의 수는 i - 1번째 집을 2번째색, 3번째색 으로 칠했을 때의
# 최소 비용에 i번째 집의 1번째 색 비용을 더한 값이다.

import sys

input = sys.stdin.readline

N = int(input())
dp = []

for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, len(dp)):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] += min(dp[i - 1][1], dp[i - 1][0])

print(min(dp[N - 1]))
