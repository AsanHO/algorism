def solution(a, b):
    arr = [a, b]
    arr.sort()
    result = 0
    for i in range(arr[0], arr[1]+1, 1):
        result += i
    return result


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))
