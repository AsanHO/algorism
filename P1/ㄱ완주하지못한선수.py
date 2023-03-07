import collections as col

# 리스트보다 딕셔너리가 효율성이 수십배 빠르다. 이유: 해싱을 사용하기 때문


def solution(participant, completion):
    dic = col.Counter(participant)
    for i in completion:
        if dic[i] != 0:
            dic[i] = dic[i]-1
    for i, j in dic.items():
        if j == 1:
            return i


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],
      ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
