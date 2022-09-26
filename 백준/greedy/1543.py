word = input()
search = input()

answer = 0
while len(word) != 0:
    start = word.find(search)
    if start != -1:
        end = start + len(search)
        word = word[end:]
        answer += 1
    else:
        break

print(answer)
