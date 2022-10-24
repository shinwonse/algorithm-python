# 15649 N과 M (1)

N, M = map(int, input().split())
s = []


def dfs():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(1, N + 1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()


dfs()
