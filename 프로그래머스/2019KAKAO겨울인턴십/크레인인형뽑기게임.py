def solution(board, moves):
    answer = 0  # 정답 담을 변수
    stack = []  # 바구니 스택

    # 어떻게 인형뽑기가 생겨먹었나 찍어봄
    # for row in board:
    #     print(row)

    # moves 배열에서 move 원소 하나씩 돌아보면서
    for move in moves:
        # 인형뽑기를 돌아봄, 이 때 i가 0부턴데 예를들어 board[0][0]이 맨 왼쪽 아래가 아니라 맨 위쪽 위라는걸 헷갈리지 말 것
        for i in range(len(board)):
            # 여튼 맨 위부터 보다가 인형을 발견하면
            if board[i][move - 1] != 0:
                # 바구니에 담아버리고
                stack.append(board[i][move - 1])
                # 그 인형은 뽑았으니까 그 자리는 0으로
                board[i][move - 1] = 0

                # 바구니에 인형이 한 개 이상 들어있으면 이제 짝을 맞춰봄
                if len(stack) > 1:
                    # 맨 위에꺼랑 그 밑에꺼가 같은 인형이라면
                    if stack[-1] == stack[-2]:
                        # 팝 팝
                        stack.pop(-1)
                        stack.pop(-1)
                        # 인형은 두 개씩 터지므로 두 개를 더함
                        answer += 2
                break
    return answer
