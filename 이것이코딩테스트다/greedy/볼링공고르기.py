n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

# 볼링공 무게별 개수
for x in data:
    array[x] += 1

result = 0
# 볼링공 하나씩 돌면서
for i in range(1, m + 1):
    n -= array[i]  # A가 선택한 볼링공 (무게가 i인 볼링공의 개수 제외)
    result += array[i] * n

print(result)
