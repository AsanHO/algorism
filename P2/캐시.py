from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    runtime = 0
    cities = list(map(lambda x: x.lower(), cities))
    for city in cities:
        if city in cache:
            runtime += 1
            cache.pop()
            cache.append(city)
        else:
            runtime += 5
            if cacheSize == 0:
                continue
            elif len(cache) >= cacheSize:
                cache.popleft()
                cache.append(city)
            else:
                cache.append(city)
    return runtime


print(solution(3, ["a", "b", "c", "a"]))  # 16
print(solution(3, ["a", "b", "c", "a", "b"]))  # 17
print(solution(3, ["a", "b", "c", "a", "b", "d", "c"]))  # 27
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
