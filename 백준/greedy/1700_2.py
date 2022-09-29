N, K = map(int, input().split())
items = list(map(int, input().split()))

tab = []
cnt = 0

for i, item in enumerate(items):
    # 이미 꽂혀 있는 거면 아무것도 안하고
    if item in tab:
        continue
    # 비어 있다면 꽂고
    if len(tab) < N:
        tab.append(item)
    # 꽉 차 있다면 가장 나중에 사용할 아이템부터 뽑음
    else:
        val = 0
        idx = -1
        tmp = items[i:]
        cnt += 1
        # 꽂혀 있는 것 중에서
        for x in tab:
            # 나중에 사용할 아이템이 있다면
            if x in tmp:
                target = tmp.index(x)
                if idx < target:
                    idx = target
                    val = x
            # 나중에 사용할 아이템이 없다면
            else:
                val = x
                break
        tab[tab.index(val)] = item

print(cnt)
