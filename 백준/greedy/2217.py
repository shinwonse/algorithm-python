n = int(input())
rope_arr = []
for _ in range(n):
    rope_arr.append(int(input()))
rope_arr.sort()
max_arr = []
for i in range(n):
    max_arr.append(rope_arr[i] * (n - i))
print(max(max_arr))
