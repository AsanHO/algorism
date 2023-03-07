def solution(X, Y):
    xarr = {str(n): 0 for n in range(10)}
    yarr = {str(n): 0 for n in range(10)}
    for x in X:
        xarr[x] += 1
    for y in Y:
        yarr[y] += 1
    answer = ""
    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(xarr[k], yarr[k])
        if answer == '' and k == '0' and iternum != 0:
            return "0"
        answer = ''.join([answer, k*iternum])
    if answer == '':
        return "-1"
    else:
        return answer


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))
