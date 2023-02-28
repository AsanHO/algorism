def solution(n):
    answer = -1
    num = n**0.5
    if num == int(num):
        answer = (num+1)**2
    return answer


print(solution(121))
print(solution(3))
print(solution(1))
print(121**0.5)
