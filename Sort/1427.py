import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T=(input())
arr=[]
for i in T:
    arr.append(i)
arr.sort()

for i in range(len(arr)):
    print(arr.pop(), end="")
