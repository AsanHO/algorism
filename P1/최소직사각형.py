def solution(sizes):
    sort = []
    for i in sizes:
        i.sort()
        sort.append(i)
    x = []
    y = []
    for i in range(len(sort)):
        x.append(sort[i][0])
        y.append(sort[i][1])
    return max(x)*max(y)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
