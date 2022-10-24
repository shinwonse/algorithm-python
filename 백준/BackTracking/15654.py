# 15654 N과 M (5)

N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
s = []


def dfs():
    if len(s) == M:
        print(" ".join(map(str, s)))

    for i in range(N):
        if num[i] in s:
            continue

        s.append(num[i])
        dfs()
        s.pop()


dfs()
