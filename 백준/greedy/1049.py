N, M = map(int, input().split())

min_package = 1001
min_single = 1001

for _ in range(M):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

answer = 0

if min_package > min_single * 6:
    answer += N * min_single
else:
    answer += (N // 6) * min_package
    if N % 6 * min_single > min_package:
        answer += min_package
    else:
        answer += (N % 6) * min_single

print(answer)
