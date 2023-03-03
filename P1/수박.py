def solution(n):
    is_su = True
    answer = ""
    for _ in range(n):
        if is_su == True:
            answer += "수"
        else:
            answer += "박"
        is_su = not is_su
    return answer


print(solution(3))
