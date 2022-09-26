import heapq
import sys

input = sys.stdin.readline

N = int(input())
lecture_list = []
for _ in range(N):
    start, end = map(int, input().split())
    lecture_list.append((start, end))
lecture_list.sort()

room = []
heapq.heappush(room, lecture_list[0][1])

for i in range(1, N):
    if lecture_list[i][0] < room[0]:
        heapq.heappush(room, lecture_list[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture_list[i][1])

print(len(room))
