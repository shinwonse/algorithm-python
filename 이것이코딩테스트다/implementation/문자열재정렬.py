# s = input()
# str_arr = []
# num_arr = []
# for i in range(len(s)):
#     if s[i].isdigit():
#         num_arr.append(s[i])
#     else:
#         str_arr.append(s[i])
# str_arr.sort()
# ans_str = ""
# for i in str_arr:
#     ans_str += i
# print(ans_str + str(sum(map(int, num_arr))))

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print("".join(result))
