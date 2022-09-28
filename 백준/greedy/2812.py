N, K = map(int, input().split())
num = list(input())
temp_k = K
result = []

for i in range(N):
    while temp_k and result:
        if result[-1] < num[i]:
            result.pop()
            temp_k -= 1
        else:
            break
    result.append(num[i])

print("".join(result[: N - K]))
