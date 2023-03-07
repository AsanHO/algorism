def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    try:
        int(s)
        return True
    except:
        return False


print(solution("a234"))
print(solution("1234"))


def alpha_string46(s):
    # 함수를 완성하세요
    return s.isdigit() and len(s) in [4, 6]
