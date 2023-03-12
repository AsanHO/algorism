# 스택을 사용
def solution(s):
    stack = []
    for c in s:
        print(stack)
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return 0
    else:
        return 1


print(solution("baabaa"))
print(solution("cdcd"))
