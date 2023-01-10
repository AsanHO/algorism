import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

x,y,w,h = map(int,input().split())

arr =[]
arr.append(h-y)
arr.append(y)
arr.append(x)
arr.append(w-x)
arr.sort()

print(arr[0])