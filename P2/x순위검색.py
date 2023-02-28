from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    # info가 통과 가능한 쿼리만들기
    infoDict = {}
    for x in info:
        make_case(x, infoDict)
    for key in infoDict.keys():
        infoDict[key].sort()
    for i in infoDict:
        print(i)


def make_case(x, infoDict):
    tempArr = x.split(" ")
    score = int(tempArr[-1])
    for idx in range(5):
        # 경우의 수 만큼 케이스를 만든다.
        for c in combinations(tempArr[:-1], idx):
            key = "".join(c)
            if key in infoDict:
                infoDict[key].append(score)
            else:
                infoDict[key] = [score]


def find_answer(key, queryScore, infoDict):
    if key in infoDict:
        return len(infoDict[key]) - bisect_left(infoDict[key], queryScore)
    return 0


a = solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
    "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])
