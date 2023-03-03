def solution(hp):
    captain = hp // 5
    hp = hp % 5
    print(f"장군개미 : {captain}")
    sergeant = hp // 3
    print(f"병정개미 : {sergeant}")
    hp = hp % 3
    private = hp // 1
    print(f"일개미 : {private}")
    return captain + sergeant + private


print(solution(23))
print(solution(24))
print(solution(999))
