import sys

input = sys.stdin.readline

N = int(input())
choo = list(map(int, input().split(" ")))
choo.sort()

target = 1
for num in choo:
    if target < num:
        break

    target += num

print(target)
