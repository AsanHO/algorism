def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in arr:
        if answer[-1] == i:
            continue
        answer.append(i)
    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))
