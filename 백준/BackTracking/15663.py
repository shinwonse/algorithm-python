# 15663 N과 M (9)

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * N
temp = []


def dfs():
    if len(temp) == M:
        print(" ".join(map(str, temp)))
        return
    remember_me = 0
    for i in range(N):
        if not visited[i] and remember_me != num[i]:
            visited[i] = True
            temp.append(num[i])
            remember_me = num[i]
            dfs()
            visited[i] = False
            temp.pop()


dfs()
