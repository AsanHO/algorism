def solution(n, m):
    answer = []
    nl = []
    ml = []
    get_divide(n, nl)
    get_divide(m, ml)
    for i in nl:
        for j in ml:
            if i == j:
                answer = []
                answer.append(i)
                break
    answer.append(n*m//answer[0])
    return answer


def get_divide(num, li):
    for i in range(1, num+1, 1):
        if num % i == 0:
            li.append(i)


print(solution(3, 12))
print(solution(2, 5))
