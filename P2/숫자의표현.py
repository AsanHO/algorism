def solution(n):
    count = 0
    for i in range(1, n+1):
        result = track(i, n)
        if result == True:
            count += 1
    return count


def track(add_num, n):
    if add_num == n:
        return True
    elif add_num > n:
        return False
    add_num += add_num + 1
    return track(add_num, n)


print(solution(15))
