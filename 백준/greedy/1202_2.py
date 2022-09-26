import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

gem_arr = []
bag_arr = []

for _ in range(N):
    weight, value = map(int, input().split())
    heapq.heappush(gem_arr, (weight, value))

for _ in range(K):
    capacity = int(input())
    heapq.heappush(bag_arr, capacity)

answer = 0
capable_gem = []

for _ in range(K):
    capacity = heapq.heappop(bag_arr)

    while gem_arr and capacity >= gem_arr[0][0]:
        weight, value = heapq.heappop(gem_arr)
        heapq.heappush(capable_gem, -value)

    if capable_gem:
        answer += -heapq.heappop(capable_gem)
    elif not gem_arr:
        break

print(answer)
