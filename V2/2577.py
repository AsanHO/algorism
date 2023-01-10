import sys
os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
Sum = str(a*b*c)
result = [0 for i in range(10)]
for i in range(10):
    for j in Sum:
        if i == int(j):
            result[i] +=1
for i in result:
    print(i)

