from itertools import combinations

N, M = list(map(int, input().split()))
data = []
chicken = []
city = []
for _ in range(N):
    data.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            city.append((i, j))
        if data[i][j] == 2:
            chicken.append((i, j))
ans = 10000
chicken_s = list(combinations(chicken, M))
print(chicken_s)
for candidate in chicken_s:
    city_dist = 0
    for j in range(len(city)):
        dist = 10000
        for x, y in candidate:
            dist = min(dist, abs(x - city[j][0]) + abs(y - city[j][1]))
        city_dist += dist
    ans = min(ans, city_dist)

print(ans)
