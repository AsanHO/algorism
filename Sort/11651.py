import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T=int(input())
arr=[]
for i in range(T):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x : (x[1],x[0]))
for i in range(T):
    print(*arr[i])