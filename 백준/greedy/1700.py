n, k = map(int, input().split())
items = list(map(int, input().split()))
tab = []
ans = 0

for i, item in enumerate(items):
    # 이미 있는 것이면 안 빼고
    if item in tab:
        continue
    # 비어 있으면 꽂고
    if len(tab) < n:
        tab.append(item)
    # 안 비어 있으면 제일 나중에 쓸 것부터 뽑음
    else:
        val = 0
        idx = -1
        ans += 1
        # 현재 인덱스 이후 아이템 리스트
        tmp = items[i:]
        for x in tab:
            if x in tmp:
                # 제일 늦게 쓸 아이템을 먼저 뽑는다
                target = tmp.index(x)
                # index 최댓값 갱신
                if idx < target:
                    idx = target
                    val = x
            # 나중에 안 쓰는거면 그냥 뽑으면 된다
            else:
                val = x
                break
        tab[tab.index(val)] = item

print(ans)
