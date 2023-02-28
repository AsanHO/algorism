def solution(n):
    n = str(n)
    arr = []
    for i in n:
        arr.append(i)
    arr.sort()
    arr.reverse()
    result = ""
    for i in arr:
        result = result+i
    result = int(result)
    return result


solution(118372)
