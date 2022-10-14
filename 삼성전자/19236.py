# 4 x 4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
import copy

array = [[None] * 4 for _ in range(4)]

# 1 <= 물고기 번호 <= 16, 같은 번호 x
# 방향은 8가지 (상하좌우, 대각선)
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 구하세요

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0


def find_fish(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == index:
                return (i, j)
    return None


def turn_left(direction):
    return (direction + 1) % 8


def move_all_fishes(arr, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(arr, i)
        if position is not None:
            x, y = position[0], position[1]
            direction = arr[x][y][1]
            for i in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]

                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        arr[x][y][1] = direction
                        arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                        break
                direction = turn_left(direction)


def get_possible_positions(arr, now_x, now_y):
    positions = []
    direction = arr[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]

        if 0 <= now_x < 4 and 0 <= now_y < 4:
            if arr[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


def dfs(array, now_x, now_y, total):
    global result
    arr = copy.deepcopy(array)

    total += arr[now_x][now_y][0]
    arr[now_x][now_y][0] = -1

    move_all_fishes(arr, now_x, now_y)

    positions = get_possible_positions(arr, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(arr, next_x, next_y, total)


dfs(array, 0, 0, 0)
print(result)
