
# 등차수열3n+3
def solution(price, money, count):
    answer = (price + price*count) * count / 2 - money
    if answer <= 0:
        answer = 0
    return answer


print(solution(3, 20, 4))
