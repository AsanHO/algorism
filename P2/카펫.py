def solution(brown, yellow):
    total_size = brown+yellow
    size = 0
    # 약수를 먼저 구할까?
    for i in range(1, total_size):
        for j in range(1, total_size):
            size = i*j
            if size == total_size:
                # answer.append([i, j])
                if i*2+j*2-4 == brown:
                    answer = [i, j]
                    answer.sort(reverse=True)
                    return answer
            elif size > total_size:
                break
        # 테두리를 브라운으로 감쌀수 있는지 검사,
        # 테두리를 어떻게 계산? 각변을 더한후 -4
# 넓이로 만들수 있는 경우의 수를 모두 만든후, 그 수에서 탐색


print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]

# 시간초과,
