# 1182 부분수열의 합

N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0


def dfs(idx, sub_sum):
    global answer

    if idx >= N:
        return

    sub_sum += nums[idx]

    if sub_sum == S:
        answer += 1

    # 현재 arr[idx]를 선택한 경우의 가지
    dfs(idx + 1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    dfs(idx + 1, sub_sum - nums[idx])


dfs(0, 0)
print(answer)
