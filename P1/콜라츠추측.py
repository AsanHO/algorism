def solution(num):
    count = 0
    result = -1
    while count <= 500:
        if num == 1:
            result = count
            break
        if num % 2 == 0:
            num = num / 2
        else:
            num = num*3+1
        count += 1
    return result


print(solution(6))
print(solution(16))
print(solution(626331))
