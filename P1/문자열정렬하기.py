import re


def solution(my_string):
    example_text_num = re.sub(r'[^0-9]', '', my_string)
    answer = list(map(int, example_text_num))
    # 문자열에서 숫자를 추출하고 싶다면 정규표현식을 사용하자.
    answer.sort()
    return answer


print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))
