import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline
T=int(input())

li = [0]*10001

for i in range(T):
    cur = int(input())
    li[cur-1] = li[cur-1]+1
    
num = 1
for i in li:
    for j in range(i):
        print(num)
    num = num +1
