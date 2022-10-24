# 1024번 수열의 합
N, L = map(int, input().split(" "))
answer = []

# 연속된 몇개의 합일지 돌려 보고
for i in range(L, 101):
    x = N - (i * (i + 1) / 2)

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                print(x + j, end=" ")
            print()
            break
else:
    print(-1)
