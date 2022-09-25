# 연속 하는 P일 중, L일 동안만 사용할 수 있다. V일 짜리 휴가를 시작
# 최대 며칠?

# 첫 날부터 무조건 사용해서 길게 사용하기

case_arr = []

while True:
    L, P, V = map(int, input().split())
    if (L, P, V) == (0, 0, 0):
        break
    # 나머지
    remain = V % P
    # 최대 연속 캠핑 일수 * 몫
    camping = L * (V // P)

    # 나머지가 사용할 수 있는 L일보다 크다면 L일만을 최대로 이용할 수 있다.
    if remain > L:
        case_arr.append(camping + L)
    # 나머지가 사용할 수 있는 L일보다 작다면 아무리 많이 사용해봤자 휴가가 부족하기 때문에 나머지만큼을 더 이용할 수 있다.
    else:
        case_arr.append(camping + remain)

for i in range(len(case_arr)):
    print("Case " + str(i + 1) + ": " + str(case_arr[i]))
