n = int(input())
dis_arr = list(map(int, input().split()))
liter_arr = list(map(int, input().split()))
amount = 0

# 맨 처음은 무조건 기름 넣고 출발해야함
# 다음 주유소가 맨 처음 주유소보다 비싸다면 그 다음 경유 거리만큼 미리 넣는 것이 이득

m = liter_arr[0]
for i in range(n - 1):
    if liter_arr[i] < m:
        m = liter_arr[i]
    amount += m * dis_arr[i]

print(amount)
