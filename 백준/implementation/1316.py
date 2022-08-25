N = int(input())

group_word = 0
for _ in range(N):
    word = input()
    error = False
    for index in range(len(word) - 1):
        if word[index] != word[index + 1]:  # 다음 문자와 다른 부분 발견시
            new_word = word[index + 1 :]  # 앞부분 자르고 그 부분부터 새로운 배열을 만들고
            # count 메서드, 문자열 안에서 찾고 싶은 문자의 개수를 찾음
            if new_word.count(word[index]) > 0:  # 만약 새로운 배열에도 아까 있던 문자가 있으면
                error = True  # 에러 발생
    if error is False:
        group_word += 1

print(group_word)
