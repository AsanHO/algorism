def solution(people, limit):
    # 가장 큰사람과 작은 사람을 태우고 안되면, 큰사람만 태우자.
    people.sort()
    count = 0
    while len(people) > 1:
        print(people)
        if people[0]+people[-1] <= limit:
            people.pop(0)
            people.pop()
            count += 1
        else:
            people.pop()
            count += 1
    count += len(people)
    return count


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3
# 코딩 접습니다~
