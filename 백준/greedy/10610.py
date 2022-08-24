n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
# 0으로 끝나지 않거나 3의 배수가 아닐 경우
# 3의 배수는 각 자릿수의 합이 3의 배수여야 한다
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))
