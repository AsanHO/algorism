lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']

# Using sort() function
lst.sort()

print(lst)


def solution(s):
    answer = list(s)
    answer.sort()
    answer = "".join(list(reversed(answer)))
    return answer


print(solution("Zbcdefg"))
