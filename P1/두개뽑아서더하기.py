import itertools


def solution(numbers):
    sets = set()
    answer = list(itertools.combinations(numbers, 2))
    for i in answer:
        sets.add(sum(i))
    return sorted(list(sets))


print(solution([2, 1, 3, 4, 1]))  # [2,3,4,5,6,7]
print(solution([5, 0, 2, 7]))  # [2,5,7,9,12]
