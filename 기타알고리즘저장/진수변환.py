# 진수 변환
def to_k_number(n, k):
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n // k
    return "".join(reversed(ret))
