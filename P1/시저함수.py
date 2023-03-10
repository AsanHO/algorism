def solution(s, n):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = list(map(lambda x: x.upper(), lower))
    answer = []
    for i in list(s):
        if i == " ":
            answer += " "
        elif i.islower():
            move(answer, lower, i, n)
            # 인덱스를 찾고 n더하기
            # 만약 길이를 넘긴다면,남은 길이를 0부터 다시
            # 대문자로 변경해서 더하기
        else:
            # 소문자로 변경해서 더하기
            move(answer, upper, i, n)
    return "".join(answer)


def move(answer, list, i, n):
    idx = list.index(i) + n
    try:
        answer.append(list[idx])
    except:
        idx = idx - len(list)
        answer.append(list[idx])
    return answer


print(solution("ab c", 1))
print(solution("z", 1))
