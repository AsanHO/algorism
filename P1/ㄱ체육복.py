def solution(n, lost, reserve):
    lost.sort()
    lost_count = len(lost)
    error = []
    for i in lost:
        print(i)
        if i in reserve:
            lost_count -= 1
            error.append(i)
            reserve.remove(i)
    for i in error:
        lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            lost_count -= 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost_count -= 1
            reserve.remove(i+1)
    return n-lost_count


print("정답", solution(5, [2, 4], [1, 3, 5]))
print("정답", solution(5, [2, 4], [3]))
print("정답", solution(3, [3], [1]))
print("정답", solution(3, [2], [2]))
print("정답", solution(5, [2, 3, 4], [1, 2, 3]))
print("정답", solution(n=5, lost=[1, 3], reserve=[2, 4]))
print("정답", solution(5, [4, 2], [3, 5]))
print("정답", solution(7, [2, 4, 7], [1, 3, 5]))
print("정답", solution(4, [2, 3], [3, 4]))
"""
1.전체 학생의 수는 2명 이상 30명 이하입니다.
2.체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
3.여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
4.여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
5.여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다.
  이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
->[2][2]일 경우를 말한다."""

# 3,7,12,13,14,24
# 5번규칙구현 -> 12,13,14
# 배열 정렬 ->  5,12
# 중복되는 친구를 먼저 정리 -> 1,6,7,24
