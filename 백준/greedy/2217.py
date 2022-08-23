n = int(input())
rope_arr = []
for _ in range(n):
    rope_arr.append(int(input()))
rope_arr.sort()
max_arr = []
for i in range(n):
    max_arr.append(rope_arr[i] * (n - i))  # 로프를 정렬한 다음에 짧은 것부터 하나 하나 빼보면서 최댓값을 배열에 넣는다
print(max(max_arr))
