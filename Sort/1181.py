import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T=int(input())
arr=set([])
for i in range(T):
    arr.add((input().strip()))

arr=list(arr)
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)