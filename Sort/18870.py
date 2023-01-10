import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 중복 제거후 리스트에 담은 후 정렬
arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i], end = ' ')