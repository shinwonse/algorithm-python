t = int(input())
button_arr = [300, 60, 10]
count_arr = [0, 0, 0]

count = 0
for i in range(3):
    while t >= button_arr[i]:
        t -= button_arr[i]
        count_arr[i] += 1
if t == 0:
    print(count_arr[0], count_arr[1], count_arr[2], sep=" ")
else:
    print(-1)

# t = int(input())
# button_arr = [300, 60, 10]
# count_arr = []
# count = 0
#
# if t % 10 != 0:
#     print(-1)
# else:
#     for i in button_arr:
#         count = t // i
#         count_arr.append(count)
#         t %= i
#     print(count_arr[0], count_arr[1], count_arr[2], sep=" ")
