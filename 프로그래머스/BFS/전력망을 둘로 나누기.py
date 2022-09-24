from collections import deque


def bfs(start, n, graph):
    queue = deque()
    queue.append(start)
    visited = [False] * (n + 1)
    visited[start] = True
    cnt = 0

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                cnt += 1

    return cnt


def solution(n, wires):
    answer = int(1e9)

    # 인접 리스트
    graph = [[] for _ in range(n + 1)]
    for x, y in wires:
        graph[x].append(y)
        graph[y].append(x)

    # 하나씩 연결을 끊고 개수 확인
    for x, y in wires:
        graph[x].remove(y)
        graph[y].remove(x)

        cnt1 = bfs(x, n, graph)
        cnt2 = bfs(y, n, graph)

        answer = min(answer, abs(cnt1 - cnt2))

        graph[x].append(y)
        graph[y].append(x)

    return answer
