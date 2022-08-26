from itertools import combinations

N, M = list(map(int, input().split()))
data = []
chicken = []
city = []
# 맵 생성
for _ in range(N):
    data.append(list(map(int, input().split())))
# 맵을 돌면서 집과 치킨집을 찾음
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            city.append((i, j))
        if data[i][j] == 2:
            chicken.append((i, j))

ans = 10000

# M개 빼고 폐업하는 조합 => 치킨집 중 M개 뽑는 조합
chicken_s = list(combinations(chicken, M))

# 그 조합을 돌면서
for candidate in chicken_s:
    city_dist = 0
    # 집을 다 돌아봄
    for j in range(len(city)):
        dist = 10000
        # 그 집과 가장 가까운 치킨 거리를 찾음
        for x, y in candidate:
            dist = min(dist, abs(x - city[j][0]) + abs(y - city[j][1]))
        # 그리고 그 치킨 거리를 도시 치킨 거리에 더함
        city_dist += dist
    # 조합 중 가장 도시 치킨 거리가 작은 녀석을 ans에 할당
    ans = min(ans, city_dist)

print(ans)
