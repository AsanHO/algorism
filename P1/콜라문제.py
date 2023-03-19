def solution(a, b, n):
    answer = 0
    empty = 0
    while n > 0:  # 남은병이 0개면 리턴
        print(n)
        empty = n % a  # 남은병 1
        send = n // a  # 반납할수 있는병 2
        answer += send*b
        n = send*b + empty
        if n / a < 1:
            break
    return answer


""" print(solution(2, 1, 20))  # 19
print(solution(3, 1, 20))  # 9 """
print(solution(3, 2, 10))  # 16
