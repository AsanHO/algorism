def solution(my_string):
    for i in ["a", "e", "i", "o", "u"]:
        answer = my_string.replace(i, "")
    return answer


print(solution("bus"))
print(solution("nice to meet you"))
