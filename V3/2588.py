import sys

os = sys.platform
if os != "linux" :
    print("명재야 보아하니 백준에서 푼게 아니구나")
    input=open("example.txt","rt").readline
else: 
    input=sys.stdin.readline

a = int(input())
b = list(str(input()))

result = 0
m = 1
for i in range(len(b)-1,-1,-1):
    x = a*int(b[i])
    result += x * m
    m = m * 10
    print(x)
print(result)