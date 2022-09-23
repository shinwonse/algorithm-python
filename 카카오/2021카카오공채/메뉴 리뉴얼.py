from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    # 구성하고자 하는 코스의 개수대로
    for c in course:
        order_combi = []
        # order 조합의 경우 구해서 order_combi에 저장
        for order in orders:
            for combi in combinations(order, c):
                order_combi.append("".join(sorted(combi)))

        most_ordered = Counter(order_combi).most_common()

        if len(most_ordered) == 0:
            continue

        max_value = most_ordered[0][1]

        for key, value in most_ordered:
            if value > 1 and value == max_value:
                answer.append("".join(key))

    return sorted(answer)
