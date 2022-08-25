# 지원자의 숫자가 최대 10만 명이므로
import sys

t = int(input())

for _ in range(t):
    n = int(input())
    lst = sorted(
        [list(map(int, sys.stdin.readline().strip().split())) for x in range(n)],
        key=lambda x: x[0],
    )
    cnt = 1
    min = lst[0][1]

    for i in range(1, n):
        if lst[i][1] < min:  # 여태 지나온 지원자들의 면접시험 성적 중 가장 좋은 면접시험 성적을 저장한다
            min = lst[i][1]
            cnt += 1
    print(cnt)
