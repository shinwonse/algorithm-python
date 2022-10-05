import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# 무게에 대한 dp 테이블 생성
dp = [0 for _ in range(K + 1)]
for item in items:
    w, v = item
    for i in range(K, w - 1, -1):
        print(i)
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[-1])
