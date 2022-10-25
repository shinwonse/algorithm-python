# 15655 N과 M (6)

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []


def dfs(start):
    if len(s) == M:
        print(" ".join(map(str, s)))

    for i in range(start, N):
        if num[i] in s:
            continue
        s.append(num[i])
        dfs(i + 1)
        s.pop()


dfs(0)
