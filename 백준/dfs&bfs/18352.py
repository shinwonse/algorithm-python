from collections import deque

# 입력 받고
n, m, k, x = list(map(int, input().split()))

# 1부터 N까지이므로 range를 n+1로 설정해야함 (인접 리스트)
graph = [[] for _ in range(n + 1)]

# 거리 정보 채우고
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 일단 거리는 -1로 모두 초기화
distance = [-1] * (n + 1)
# 출발하는 위치 거리는 0 (출발점 -> 출발점)
distance[x] = 0

# from collections import deque
q = deque([x])
# queue가 빌 때까지
while q:
    # 맨 앞에꺼를 팝하고
    now = q.popleft()
    # 그 지점에서의 거리 정보를 하나씩 돈다 ex) [2, 3]
    for next_node in graph[now]:
        if distance[next_node] == -1:
            # 인접 구간에서 거리가 1
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check is False:
    print(-1)
