A, B = input().split()

max_A = ""
min_A = ""

max_B = ""
min_B = ""

for a in A:
    if a == "5":
        max_A += "6"
        min_A += "5"
    elif a == "6":
        max_A += "6"
        min_A += "5"
    else:
        max_A += str(a)
        min_A += str(a)

for b in B:
    if b == "5":
        max_B += "6"
        min_B += "5"
    elif b == "6":
        max_B += "6"
        min_B += "5"
    else:
        max_B += str(b)
        min_B += str(b)

max_answer = int(max_A) + int(max_B)
min_answer = int(min_A) + int(min_B)

print(min_answer, max_answer)
