n = 1000 - int(input())
money_list = [500, 100, 50, 10, 5, 1]
count = 0
for i in money_list:
    count += n // i
    n %= i
print(count)
