def solution(arr):
    arr.sort()
    print(arr)
    del arr[0]
    print(arr)
    if len(arr) == 0:
        return [-1]
    return arr


print(solution([4, 3, 2, 1]))
print(solution([10]))
