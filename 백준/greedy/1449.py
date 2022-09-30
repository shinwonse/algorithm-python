N, L = map(int, input().split())
water = list(map(int, input().split()))

# 좌우 0.5만큼 간격을 줘야 한다
# => 물이 새는 곳이 1과 3이라면 길이가 2인 테이프로 그 부분만 막으면 안 되고
# 양쪽으로 0.5만큼씩 더 막아줘야 한다
# 0.5 ~ 2.5, 1.5 ~ 3.5 이렇게 막아주는 것이 최소이다.

water.sort()
start = water[0]
count = 1

for w in water[1:]:
    if w in range(start, start + L):
        continue
    else:
        start = w
        count += 1

print(count)
