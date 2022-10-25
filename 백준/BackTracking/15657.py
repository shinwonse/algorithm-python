# 15657 N과 M (8)

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []


def dfs(start):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(start, N):
        s.append(num[i])
        dfs(i)
        s.pop()


dfs(0)
