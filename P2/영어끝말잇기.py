def solution(n, words):
    # 전처리
    cur = 2
    cycle = 1
    completed_word = [words[0]]
    last = words[0][-1]

    for i in range(1, len(words)):
        # 현재단어
        curword = words[i]
        # 이미 말한 단어이거나 끝말있기가 안됬다면 리턴
        if words[i] in completed_word or last != curword[0]:
            print("탈락!")
            return [cur, cycle]
        # 아니면 계속 진행
        last = curword[-1]
        completed_word.append(curword)
        if cur == n:
            cur = 1
            cycle += 1
        else:
            cur += 1
    return [0, 0]
