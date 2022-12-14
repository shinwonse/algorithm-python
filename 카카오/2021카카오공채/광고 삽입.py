# 문자열로 입력받은 시간을 초로 환산
def str_to_int(time):
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


# 답으로 제출하기 위한 변환
def int_to_str(time):
    h = time // 3600
    h = "0" + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = "0" + str(m) if m < 10 else str(m)
    time = time % 60
    s = "0" + str(time) if time < 10 else str(time)
    return h + ":" + m + ":" + s


def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    # 타임라인에 대한 수직선을 그리고 1초당 시청자수를 누적하여 기록
    all_time = [0 for i in range(play_time + 1)]

    for l in logs:
        start, end = l.split("-")
        start = str_to_int(start)
        end = str_to_int(end)
        all_time[start] += 1
        all_time[end] -= 1

    # 구간별 시청자수 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    # 모든 구간 시청자 누적 기록
    for i in range(1, len(all_time)):
        all_time[i] = all_time[i] + all_time[i - 1]

    most_view = 0
    max_time = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                max_time = i - adv_time + 1

    return int_to_str(max_time)
