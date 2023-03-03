def solution(a, b):
    result = 0
    for i in range(a, b+1, 1):
        divisor = []
        for num in range(1, i + 1, 1):
            if i % num == 0:
                divisor.append(num)
        if len(divisor) % 2 == 0:
            result += i
        else:
            result -= i
    return result


print(solution(13, 17))
