from collections import deque

# N 아파트 단지수, K 통학버스의 정원, S 학교의 위치
N, K, S = map(int, input().split())

# 학교보다 왼쪽, 오른쪽
left = []
right = []

for _ in range(N):
    x, y = map(int, input().split())
    if x > S:
        left.append([abs(S - x), y])
    elif x < S:
        right.append([abs(S - x), y])

left = deque(sorted(left, key=lambda x: x[0], reverse=True))
right = deque(sorted(right, key=lambda x: x[0], reverse=True))

answer = 0
cur = 0

while left:
    answer += left[0][0] * 2
    while left and left[0][1] <= K - cur:  # 전부 실을 수 있는 경우
        d, h = left.popleft()
        cur += h
    if left:  # 일부만 실을 수 있는 경우
        left[0][1] -= K - cur
        cur = 0

cur = 0
while right:
    answer += right[0][0] * 2
    while right and right[0][1] <= K - cur:  # 전부 실을 수 있는 경우
        d, h = right.popleft()
        cur += h
    if right:  # 일부만 실을 수 있는 경우
        right[0][1] -= K - cur
        cur = 0

print(answer)
