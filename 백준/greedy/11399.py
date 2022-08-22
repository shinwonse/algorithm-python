n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
for i in range(n):
    for j in range(i + 1):
        result += data[j]
print(result)
