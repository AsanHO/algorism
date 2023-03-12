def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        print(format(int(arr1[i]) | int(arr2[i]), 'b'))
        answer.append(format(int(arr1[i]) | int(arr2[i]), 'b').zfill(
            n).replace('1', '#').replace('0', ' '))
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
