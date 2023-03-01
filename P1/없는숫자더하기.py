def solution(numbers):
    answer = 0
    for i in range(10):
        is_have = False
        for j in numbers:
            if i == j:
                is_have = True
                break
        if is_have == False:
            answer += i
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
print(solution([5, 8, 4, 0, 6, 7, 9]))
