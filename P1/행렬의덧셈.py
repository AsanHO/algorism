def solution(arr1, arr2):
    answer = []
    # 기준으로 하나 만들기
    length = len(arr1)
    for i in range(length):
        sum = []
        length2 = len(arr1[0])
        for j in range(length2):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
    return answer


print(solution([[1, 2], [2, 3]],
               [[3, 4], [5, 6]]))
print(solution([[1], [2]],
               [[3], [4]]))
print(solution([[1, 2, 3, 4], [2, 3, 4, 5]],
               [[3, 4, 2, 3], [5, 6, 1, 2]]))
