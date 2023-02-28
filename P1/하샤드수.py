def solution(n):
    return n % sum(list(map(int, str(n)))) == 0


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
