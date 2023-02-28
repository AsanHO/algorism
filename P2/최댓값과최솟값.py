def solution(s):
    # 분리
    s = s.split(" ")
    # 정수형으로 포맷
    s = list(map(int, s))
    MIN,MAX = min(s),max(s)
    result = f"{MIN} {MAX}"
    return result

solution("0 1 2 3")