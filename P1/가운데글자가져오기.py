def solution(numbers):
    loc = int(len(numbers) / 2)
    if len(numbers) % 2 == 0:
        # 1234 이면 [1]부터[3]까지
        return numbers[loc-1: loc+1]

    else:
        return numbers[loc]


print(solution("abcde"))
print(solution("qwer"))
